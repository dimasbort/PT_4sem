from Serializers.serializer import Serializer
import pickle
import codecs

class PickleSerializer(Serializer):

    # function that parses py-obj to pickle-str
    def parse(obj):
        pickle_str = codecs.encode(pickle.dumps(obj), "base64").decode()
        return pickle_str


    # function that unparses pickle-str to py-obj
    def unparse(pickle_str):
        py_obj = pickle.loads(codecs.decode(pickle_str.encode(), "base64"))
        return py_obj