from serializers import *



def make_ser(t):
    if (t == "json"):
        return JSON_Serializer()
    if (t == "yaml"):
        return YAML_Serializer()
    if (t == "pickle"):
        return PICKLE_Serializer()
    if (t == "toml"):
        return TOML_Serializer()



def make_sers(input_format, output_format):

    if (input_format == "json"):
        deserializer = make_ser("json")
    elif (input_format == "pickle"):
        deserializer = make_ser("pickle")
    elif (input_format == "toml"):
        deserializer = make_ser("toml")
    elif (input_format == "yaml"):
        deserializer = make_ser("yaml")
    else: raise Exception("What is it?")


    if (output_format == "json"):
        serializer = make_ser("json")
    elif (output_format == "pickle"):
        serializer = make_ser("pickle")
    elif (output_format == "toml"):
        serializer = make_ser("toml")
    elif (output_format == "yaml"):
        serializer = make_ser("yaml")
    else: 
        raise Exception("What is it?")


    return (serializer, deserializer)
