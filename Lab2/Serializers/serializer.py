import inspect
import pickle
import base64
import cloudpickle

class Serializer():
    # ----------------------- SERIALIZATION ----------------------
    def serialize(self, obj, filename="default"):
        if filename != "default":
            return self.dump(obj, filename)
        else:
            return self.dumps(obj)

    # serializing python object to string
    @classmethod
    def dump(cls, obj, filename):
        str_data = cls.parse(obj)
        opened_file = open(filename, mode = 'w', encoding='UTF-8')
        opened_file.write(str_data)
        opened_file.close()

        return str_data

    # serializing python ojbect to file
    @classmethod
    def dumps(cls, obj):
        return cls.parse(obj)

    # parsing object of python to string
    # expected to be overrided by derived class
    def parse(obj):
        raise Exception("parse is not implemented for abstract Serializer")


    # ----------------------- DESERIALIZATION ----------------------
    def deserialize(self, str_data, filename="default"):
        if filename != "default":
            return self.load(filename)
        else:
            return self.loads(str_data)

    # deserializing python object from file
    @classmethod
    def load(cls, filename):
        opened_file = open(filename, mode = 'r', encoding='UTF-8')
        str_data = opened_file.read()
        opened_file.close()

        return cls.unparse(str_data)

    # deserializing python object from string
    @classmethod
    def loads(cls, str_data):
        return cls.unparse(str_data)
            
    # unparsing string to python object
    # expected to be overrided by derived class
    def unparse(str_data):
        raise Exception("unparse is not implemented for abstract Serializer")


    # ------------ SOME EXTRA USEFUL FUNCTIONS FOR SERALIZERS -----------
    @classmethod
    def get_object_type(cls, py_obj):
        # returning true if object is class
        if inspect.isclass(py_obj):
            return 'class'

        # if not class - getting its type
        else:
            return str(type(py_obj)).split('\'')[1]

    @classmethod
    def get_object_name(cls, py_obj):
        try:
            return py_obj.__name__
        except AttributeError:
            return None

    @classmethod
    def get_class_dict(cls, class_to_serialize):
        try:
            return {key: str(val) for key, val in class_to_serialize.__dict__.items()}
        except AttributeError:
            return {}

    @classmethod
    def get_function_arguments(cls, function_to_serialize):
        list_type_args = [
            'args', 'varargs', 'varkw', 'defaults',
            'kwonlyargs', 'kwonlydefaults', 'annotations',
        ]
        try:
            return {
                arg_name: args for (
                    arg_name, args
                ) in zip(
                    list_type_args,
                    inspect.getfullargspec(function_to_serialize)
                )
            }
        except TypeError:
            return {}

    @classmethod
    def get_source_code(cls, py_obj):
        try:
            return inspect.getsource(py_obj).split('\n')
        except TypeError:
            return []


    @classmethod
    def get_base64_pickle_object(cls, py_obj):
        try:
            if (cls.is_lambda_function(py_obj)):
                pickle_str = cloudpickle.dumps(py_obj)
                b64 = base64.b64encode(pickle_str).decode('ascii')
                return b64

            return base64.b64encode(pickle.dumps(py_obj)).decode('ascii')
        except TypeError:
            return None

        
    @classmethod
    def get_object_from_base64(cls, base64_obj):
        try:
            return pickle.loads(base64.b64decode(base64_obj.encode('ascii')))
        except AttributeError:
            return None