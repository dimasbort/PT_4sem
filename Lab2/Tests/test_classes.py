import inspect


class SimpleClass():
    def __init__(self, age, gender):
        self._age = age
        self._gender = gender

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    def __str__(self):
        return (f"{self._age}, {self._gender}")


class ComplicatedClass():
    def __init__(self, name, date, hm):
        self._name = name
        self._date = date
        self._arr = list(range(10))
        self._human = hm

    def get_name(self):
        return self._name

    def get_date(self):
        return self._date

    def get_human(self):
        return self._human

    def print_st_info(self):
        print(f"name: {self._name}, date: {self._date}, arr: {self._arr}, human: {self._human}")

def SimpleFunction(age):
    print(age)
    print("\n")

def RecursiveFunction(n):
    if n == 0:
        return 1
    return RecursiveFunction(n-1) * n

global_var = 5

def GlobalFunction(n):
    return n + global_var


hm1 = SimpleClass(20, "Male")
st1 = ComplicatedClass("Vasya Pupkin", "01.02.2000", SimpleClass(25, "Male"))

tuple_one = (10, 2.13, "square", 89, 'C')
list_one = [66.25, 333, 333, 1, 1234.5]

add_one = lambda x: x + 1