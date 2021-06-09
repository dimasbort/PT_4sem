from Serializers.serializer import Serializer
import json
import inspect

class JsonSerializer(Serializer):
    
    # function that parses py-obj to json-str
    def parse(py_obj):
        return JsonSerializer.serialize_object(py_obj)


    # function that unparses json-str to py-obj
    def unparse(json_str):
        return JsonSerializer.deserialize_str(json_str)


    @classmethod
    def serialize_object(cls, py_obj):
        obj_type = cls.get_object_type(py_obj)

        # trying to serialize like it is built-in type
        is_default_serializible = cls._is_json_serializible(py_obj)
 
        json_str = {
            'object': repr(py_obj),
            'type': obj_type,
            'serializable_by_default': is_default_serializible,
            'name': cls.get_object_name(py_obj),
            'value': py_obj if is_default_serializible
                            else None,
            'dict_class': cls.get_class_dict(py_obj),
            'args': cls.get_function_arguments(py_obj),
            'code': cls.get_source_code(py_obj),
            'base64': cls.get_base64_pickle_object(py_obj)
        }
    

        return json.dumps(json_str)

    @classmethod
    def _is_json_serializible(cls, py_obj):
        try:
            json.dumps(py_obj)
            return True
        except TypeError:
            return False

    @classmethod
    def is_lambda_function(cls, py_obj):
        parts = py_obj.__name__.split('<')
        name_str = parts[1]
        parts = name_str.split('>')
        name_str = parts[0]     

        if name_str == "lambda":
            return True
        parts = name_str.split('>')
        name_str = parts[0]     

        if name_str == "lambda":
            return True
        else:
            return False

    @classmethod
    def deserialize_str(cls, json_str):
        json_dict = json.loads(json_str)
        return cls.get_object_from_base64(json_dict.get('base64'))