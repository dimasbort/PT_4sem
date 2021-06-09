import sys
sys.path.append('../')

import unittest
from Serializers.json_serializer import JsonSerializer
from test_classes import *

serializer = JsonSerializer()

class TestJsonSerialization(unittest.TestCase):
    # testing whether simple function is correct
    def test_simple_function(self):
        func_simple = serializer.serialize(SimpleFunction)
        simple_func = serializer.deserialize(func_simple)
        self.assertEqual(simple_func(25), SimpleFunction(25))

    # testing recursive function is correct
    def test_complicated_function(self):
        func_compl = serializer.serialize(RecursiveFunction)
        recur_func = serializer.deserialize(func_compl)
        self.assertEqual(recur_func(5), RecursiveFunction(5))

    # testing function with global variable
    def test_global_function(self):
        func_glob = serializer.serialize(GlobalFunction)
        glob_func = serializer.deserialize(func_glob)
        self.assertEqual(glob_func(5), GlobalFunction(5))

    # testing methods in class are done correctly
    def test_simple_class(self):
        class_simpl = serializer.serialize(SimpleClass)
        simple_class = serializer.deserialize(class_simpl)
        obj1 = simple_class(20, "Male")
        obj2 = SimpleClass(20, "Male")
        self.assertEqual(obj1.get_age(), obj2.get_age())

    # testing object is instance of original class
    def test_compl_class(self):
        class_compl = serializer.serialize(ComplicatedClass)
        compl_class = serializer.deserialize(class_compl)
        obj1 = compl_class("Dmitry", "25.10.2000", SimpleClass(25, "Male"))
        self.assertIsInstance(obj1, ComplicatedClass)

    # testing object is instance of original class
    def test_simple_obj(self):
        obj_simpl = serializer.serialize(hm1)
        simple_object = serializer.deserialize(obj_simpl)
        self.assertIsInstance(simple_object, SimpleClass)

    # testing methods of object
    def test_compl_obj(self):
        obj_compl = serializer.serialize(st1)
        compl_obj = serializer.deserialize(obj_compl)
        self.assertEqual(compl_obj.get_date(), st1.get_date())

    # testing tuple
    def test_tuple(self):
        tupl = serializer.serialize(tuple_one)
        tuple_obj = serializer.deserialize(tupl)
        self.assertEqual(tuple_obj, tuple_one)

    # testing list
    def test_list(self):
        list_test = serializer.serialize(list_one)
        list_obj = serializer.deserialize(list_test)
        self.assertEqual(list_obj, list_one)



if __name__ == '__main__':
    unittest.main()