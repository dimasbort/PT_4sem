from Serializers.serializer import Serializer
from Serializers.json_serializer import *
import yaml

class YamlSerializer(Serializer):

    # function that parses py-obj to json-str
    def parse(obj):
        
        # getting dictionary
        dict_obj = JsonSerializer.serialize_object(obj)

        #yaml dump of dictionary to yaml-object
        return yaml.dump(dict_obj)

    # function that unparses yaml-obj to py-obj
    def unparse(str_data):

        # getting dictionary
        dict_obj = yaml.load(str_data, Loader=yaml.FullLoader)

        return JsonSerializer.deserialize_str(dict_obj)