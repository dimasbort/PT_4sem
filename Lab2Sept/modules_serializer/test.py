import unittest
from modules_serializer.serializers import *
from modules_serializer.file1 import *

user = User()
clas = User
func = GGG
test = Test()
lm = lambda x, y: x * y
yaml_s = YAML_S()
toml_s = TOML_S()
json_s = JSON_S()
pickle_s = PICKLE_S()
y_path = "/home/dimasbort/PycharmProjects/Lab2Sept/docs/input.yaml"
j_path = "/home/dimasbort/PycharmProjects/Lab2Sept/docs/input.json"
t_path = "/home/dimasbort/PycharmProjects/Lab2Sept/docs/input.toml"
p_path = "/home/dimasbort/PycharmProjects/Lab2Sept/docs/input.pickle"
j_dump_str = json_s.dumps(clas)
p_dumps_str = pickle_s.dumps(clas)


class TestSerializers(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None


    def test_yaml_load(self):
        yaml_s.dump(user, y_path)
        self.assertEqual(yaml_s.load(y_path).__class__.__name__,
                         user.__class__.__name__)

    def test_json_load(self):
        json_s.dump(user, j_path)
        self.assertEqual(json_s.load(j_path).__class__.__name__,
                         user.__class__.__name__)

    def test_pickle_load(self):
        pickle_s.dump(user, p_path)
        self.assertEqual(pickle_s.load(p_path).__class__.__name__,
                         user.__class__.__name__)

    def test_toml_load(self):
        toml_s.dump(user, t_path)
        self.assertEqual(toml_s.load(t_path).__class__.__name__,
                         user.__class__.__name__)

    def test_pickle_loads(self):
        self.assertEqual(pickle_s.loads(pickle_s.dumps(user)).__class__.__name__, user.__class__.__name__)

    def test_json_loads(self):
        self.assertEqual(json_s.loads(json_s.dumps(user)).__class__.__name__, user.__class__.__name__)

    def test_toml_loads(self):
        self.assertEqual(toml_s.loads(toml_s.dumps(user)).__class__.__name__, user.__class__.__name__)

    def test_yaml_loads(self):
        self.assertEqual(yaml_s.loads(yaml_s.dumps(user)).__class__.__name__, user.__class__.__name__)

    def test_pickle_load_function(self):
        pickle_s.dump(func, p_path)
        self.assertEqual(pickle_s.load(p_path)(2, -2), 10)

    def test_json_load_function(self):
        json_s.dump(func, j_path)
        self.assertEqual(json_s.load(j_path)(-2, 3), 11)

    def test_toml_load_function(self):
        toml_s.dump(func, t_path)
        self.assertEqual(toml_s.load(t_path)(-10, -10), -10)

    def test_yaml_load_function(self):
        yaml_s.dump(user, y_path)
        self.assertEqual(yaml_s.load(y_path).s(), "Dimasik")

    def test_pickle_loads_class(self):
        t_str = pickle_s.dumps(test)
        self.assertEqual(pickle_s.loads(t_str).home, "Brest")

    def test_yaml_loads_class(self):
        t_str = yaml_s.dumps(test)
        self.assertEqual(yaml_s.loads(t_str).home, "Brest")

    def test_toml_loads_class(self):
        t_str = toml_s.dumps(test)
        self.assertEqual(toml_s.loads(t_str).home, "Brest")

    def test_json_loads_class(self):
        t_str = json_s.dumps(test)
        self.assertEqual(json_s.loads(t_str).home, "Brest")

    def test_lamda_load(self):
        t_str = json_s.dump(lm, j_path)
        self.assertEqual(json_s.load(j_path)(5, 10), 50)

    def test_dumps_lamda(self):
        t_str = json_s.dump(lm, j_path)
        lam = json_s.load(j_path)
        self.assertEqual(lam.__class__, lm.__class__)

    def test_json_dumps(self):
        self.assertEqual(json_s.dumps(clas), j_dump_str)

    def test_pickle_dump(self):
        self.assertEqual(pickle_s.dumps(clas), p_dumps_str)

