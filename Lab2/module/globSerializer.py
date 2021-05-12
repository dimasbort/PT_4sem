#from modules.options import *
#from modules.classes import *
import inspect
import types
import dis
import opcode
import weakref
from types import FunctionType


_extract_code_globals_cache = weakref.WeakKeyDictionary()
STORE_GLOBAL = opcode.opmap['STORE_GLOBAL']
DELETE_GLOBAL = opcode.opmap['DELETE_GLOBAL']
LOAD_GLOBAL = opcode.opmap['LOAD_GLOBAL']
GLOBAL_OPS = (STORE_GLOBAL, DELETE_GLOBAL, LOAD_GLOBAL)
def _extract_code_globals(co):
    out_names = _extract_code_globals_cache.get(co)
    if out_names is None:
        names = co.co_names
        out_names = {names[oparg] for _, oparg in _walk_global_ops(co)}
        if co.co_consts:
            for const in co.co_consts:
                if isinstance(const, types.CodeType):
                    out_names |= _extract_code_globals(const)
        _extract_code_globals_cache[co] = out_names
    return out_names
def _walk_global_ops(code):
    for instr in dis.get_instructions(code):
        op = instr.opcode
        if op in GLOBAL_OPS:
            yield op, instr.arg

class Serializer:

    def object_to_dict(self, obj):
        if str(obj).__contains__('object'):
            x = {'__type__' : 'object', '__class__' : obj.__class__.__name__}
            for pol in obj.__dir__():
                if not pol.startswith('__'):
                    attr = getattr(obj, pol)
                    if callable(attr):
                        if len(inspect.getfullargspec(attr).args) > 1:
                            x[pol] = self.func_to_dict(attr)
                        elif "<class.__main__" in attr.__class__:
                            x[pol] = self.object_to_dict(attr)
                        else:
                            x[pol] = attr
            return x
        else:
            raise Exception("Not an object")


    def class_to_dict(self, cla):
        if cla.__class__.__name__=='type':
            x = {'__type__' : 'class', '__class__' : cla}
            for pol in dir(cla):
                if not pol.startswith('__'):
                    attr = getattr(cla, pol)
                    if "<class 'type'>" in attr:
                        x[pol] = self.class_to_dict(attr)
                    elif "<class.__main__" in attr:
                        x[pol] = self.object_to_dict(attr)
                    elif callable(attr):
                        if len(inspect.getfullargspec(attr).args) > 1:
                            x[pol] = self.func_to_dict(attr)
                    else:
                        x[pol] = attr
            return x
        else:
            raise Exception("Not a class")



    def func_to_dict(self, obj):

        argumets = {}
        dicti = {'__type__': 'function'}

        argumets['co_argcount'] = repr(obj.__code__.co_argcount)
        argumets['co_posonlyargcount'] = repr(obj.__code__.co_posonlyargcount)
        argumets['co_kwonlyargcount'] = repr(obj.__code__.co_kwonlyargcount)
        argumets['co_nlocals'] = repr(obj.__code__.co_nlocals)
        argumets['co_stacksize'] = repr(obj.__code__.co_stacksize)
        argumets['co_flags'] = repr(obj.__code__.co_flags)
        argumets['co_code'] = obj.__code__.co_code.hex()
        argumets['co_consts'] = list(obj.__code__.co_consts)
        argumets['co_names'] = list(obj.__code__.co_names)
        argumets['co_varnames'] = list(obj.__code__.co_varnames) 
        argumets['co_filename'] = repr(obj.__code__.co_filename)
        argumets['co_name'] = repr(obj.__code__.co_name)
        argumets['co_firstlineno'] = repr(obj.__code__.co_firstlineno)
        argumets['co_lnotab'] =obj.__code__.co_lnotab.hex()
        dicti['args'] = argumets

        gl = _extract_code_globals(obj.__code__)
        gla = {}
        gla['__builtins__'] = '<module \'builtins\' (built-in)>'

        for glob in gl:
            if glob in globals() :
                gla[glob] = repr(globals().get(glob))
        dicti['globals'] = gla

        return dicti



    def dict_to_func(self, dic):
        list_of_args=[]
        import importlib
        list_of_globals = dic["globals"]

        for glob in list_of_globals:

            if str.isnumeric(list_of_globals[glob]):
                list_of_globals[glob]=int(list_of_globals[glob])

            else:

                if list_of_globals[glob].find("module") > 0 :
                    if list_of_globals[glob].find("from") > 0 :
                        value = list_of_globals[glob][9:list_of_globals[glob].find("from")-2]
                        list_of_globals[glob] = importlib.import_module(value)    

        for arg in dic:
            if arg == "args":
                for value_args in dic[arg]:
                    list_of_args.append(dic[arg][value_args])  

        code = types.CodeType(int(list_of_args[0]),int(list_of_args[1]),int(list_of_args[2]),
        int(list_of_args[3]),int(list_of_args[4]),int(list_of_args[5]),
        bytes.fromhex(list_of_args[6]),tuple(list_of_args[7]),tuple(list_of_args[8]),
        tuple(list_of_args[9]),list_of_args[10],list_of_args[11],int(list_of_args[12]),
        bytes.fromhex(list_of_args[13]))

        return types.FunctionType(code,list_of_globals)        


    def dict_to_object(self, json):
        class_name = globals()[json['__class__']]
        init_args = inspect.getfullargspec(class_name).args
        args = {}
        for arg in init_args:
            if arg in json:
                args[arg] = json[arg]
        obj = class_name(**args) 
        for attr in obj.__dir__():
            if isinstance(getattr(obj, attr), dict) and not attr.startswith('__'):
                object_attr  = self.dict_to_object(getattr(obj, attr))
                setattr(obj, attr, object_attr)            
            elif not attr.startswith('__') and attr not in args:
                object_attr = getattr(obj, attr)
                if not callable(object_attr):
                    setattr(obj, attr, json[attr])
        return obj


    def dict_to_class(self, json):
        vars = {}
        for attr in json:
            if not isinstance(json[attr], dict) and not attr.startswith('__'):
                vars[attr] = json[attr]
            elif isinstance(json[attr], dict) and not attr.startswith('__'):
                if json[attr]['__type__'] == 'function':
                    vars[attr] = self.dict_to_func(json[attr]) 
                
        return type("User", (object, ), vars)  




    def make_dict(self, obj, typ):
        A = self.input_correct(obj, typ)
        if not A:
            raise Exception("Incorrect!")
        myDict = None
        if typ == 'function':
            myDict = self.func_to_dict(obj)
        elif typ == 'class':
            myDict = self.class_to_dict(obj)
        elif typ == 'object':
            myDict = self.object_to_dict(obj)
        return myDict

    def make_party(self, dct):
        party = None
        if dct['__type__'] == 'function':
            party = self.dict_to_func(dct)
        elif dct['__type__'] == 'class':
            party = self.dict_to_class(dct)
        elif dct['__type__'] == 'object':
            party = self.dict_to_object(dct)
        return party

    
    def getDictionary(self, obj, tp):
        check = (False, True)[self.input_correct(obj, tp)]
        if not check: raise Exception("Incorrect input!")
        dict_obj = self.make_dict(obj, tp)
        return dict_obj

    def get_type(self, obj):
        if (obj.__class__.__name__ == "function"): 
           return "function"
        elif obj.__class__.__name__ == "type":
            return "class"
        elif str(obj).__contains__("object"):
          return "object"
        else: 
          raise Exception("Invalid entity!")
        

    def input_correct(self, obj, typ):
        if obj.__class__.__name__ == 'function' and typ == 'function':
            return True
        elif obj.__class__.__name__ == 'type' and typ == 'class':
           return True
        elif str(obj).__contains__('object')  and typ == 'object':
           return True
        else:
           return False



