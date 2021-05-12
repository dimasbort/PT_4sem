#import inspect
import json
import yaml
import toml
import pickle
from globSerializer import Serializer

  
    
class JSON_Serializer(Serializer):
    
    def dump(self, obj, fp, typ):
        diction = super().make_dict(obj, typ)
        with open(fp, "w") as file:
            json.dump(diction, file)
            file.close()

    def dumps(self, obj, typ):
        diction = super().make_dict(obj, typ)
        json_obj = json.dumps(diction)
        return json_obj

    def loads(self, s):
        diction = json.load(s)
        party = super().make_party(diction)
        return party
    
    def load(self, fp):
        diction = None
        with open(fp, "r", encoding='utf-8') as file:
            diction = json.load(file)
            file.close()
        party = super().make_party(diction)
        return party


class TOML_Serializer(Serializer):
    
    def dump(self, obj, fp, typ):
        diction = super().make_dict(obj, typ)
        with open(fp, "w") as file:
            toml.dump(diction, file)
            file.close()

    def dumps(self, obj, typ):
        diction = super().make_dict(obj, typ)
        json_obj = toml.dumps(diction)
        return json_obj

    def loads(self, s):
        diction = toml.load(s)
        party = super().make_party(diction)
        return party
    
    def load(self, fp):
        diction = None
        with open(fp, "r") as file:
            diction = toml.load(file)
            file.close()
        party = super().make_party(diction)
        return party


class YAML_Serializer(Serializer):
    
    def dump(self, obj, fp, typ):
        diction = super().make_dict(obj, typ)
        with open(fp, "w") as file:
            yaml.dump(diction, file)
            file.close()

    def dumps(self, obj, typ):
        diction = super().make_dict(obj, typ)
        json_obj = yaml.dump(diction)
        return json_obj

    def loads(self, s):
        diction = yaml.load(s)
        party = super().make_party(diction)
        return party
    
    def load(self, fp):
        diction = None
        with open(fp, "r") as file:
            diction = yaml.load(file)
            file.close()
        party = super().make_party(diction)
        return party


class PICKLE_Serializer(Serializer):
    
    def dump(self, obj, fp, typ):
        diction = super().make_dict(obj, typ)
        with open(fp, "wb") as file:
            pickle.dump(diction, file)
            file.close()

    def dumps(self, obj, typ):
        diction = super().make_dict(obj, typ)
        json_obj = pickle.dump(diction)
        return json_obj

    def loads(self, s):
        diction = pickle.load(s)
        party = super().make_party(diction)
        return party
    
    def load(self, fp):
        diction = None
        with open(fp, "rb") as file:
            diction = pickle.load(file)
            file.close()
        party = super().make_party(diction)
        return party














if __name__ == '__main__':
    class Non:
       def fact(self, n):
           print('Poka')

    func = lambda x, y: x + y

    def f(n):
        a=1
        print('Poka')
    y=JSON_Serializer
    #print(y.dumps(Non,'class'))
    
    x=Non().fact
    
    print(f.__code__.co_varnames)