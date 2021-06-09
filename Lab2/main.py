from Serializers.serializer import Serializer
from factory import Factory
import argparse
from Tests.test_classes import *
import cloudpickle
import pickle

def main():
    # ----------------------------- ARGPARSE ----------------------------

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="enter path to file")
    parser.add_argument("--format", type=str, help="enter format to convert")
    args = parser.parse_args()
    file_path = getattr(args, 'path')
    new_format_type = getattr(args, 'format')

    print(file_path)
    print(new_format_type) 

    # --------------------------- UTILITY WORK ------------------------------

    str_parts = file_path.split(".")
    initial_format_type = str_parts[1]
    serializer = Factory.create_serializer(initial_format_type)
    py_obj = serializer.deserialize("", file_path)

    serializer = Factory.create_serializer(new_format_type)

    new_file_name = str_parts[0] + "." + new_format_type
    serializer.serialize(py_obj, new_file_name)

if __name__ == '__main__':
    exit(main())