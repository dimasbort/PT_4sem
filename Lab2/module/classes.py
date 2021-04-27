
class Student:

    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty 
        
    l = lambda x, y: x * y

s = 5
k = 2
z = 5

class Car:

    def __init__(self, color):
        self.color = color


class User:

    name = "Dimas"
    adress = "Brest"

    def func(self, x1, x2):
        return x1 + x2

    l = lambda x, y: x + y

user = User()
ca = Car("Blue")
st2 = Student("Sasha", None)
st1 = Student("Pasha", "Ksis")  


def func(x, y, z):
    return x + y + z


def f(x, y):
    global s
    return x + y + s


lambd = lambda x, y: x + y



def return_string():
    toml_serializer = create_serializer('toml')
    yaml_serializer = create_serializer('yaml')

    string_toml = toml_serializer.dump(f, 'docs/input.toml', 'function')
    print(string_toml)
    string_yaml = yaml_serializer.dump(lambd, 'docs/input.yaml', 'function')

    return (string_toml, string_yaml)
    



