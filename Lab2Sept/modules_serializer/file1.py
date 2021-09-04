from modules_serializer.file2 import t


class Test:
    home = "Brest"
    isHome = True
    f = [1, 2]
    dic = {"field": [[1, 2], [3, 4]]}


class User:
    name = 'Dimasik'
    d = [True, False]
    k = 5
    typ = None
    tup = ({"r": None})

    def s(self):
        return self.name


class Dima:
    Lab = True
    Marks = ["exellent", "super"]
    Days = (4, 11)


def GGG(a, b):
    return a + b + t