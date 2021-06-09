class Vector:
    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, other):
        for ind in range(len(self.numbers)):
            if len(other.numbers) > ind:
                self.numbers[ind] += other.numbers[ind]

    def __mul__(self, other):
        for ind in range(len(self.numbers)):
            self.numbers[ind] *= other

    def mult_scalar(self, secondV, angle):
        return sum([self.numbers[i] * secondV.numbers[i] for i in range(len(a))])

    def __gt__(self, other):
        for ind in range(len(self.numbers)):
            if self.numbers[ind] < other.numbers[ind]:
                return False
        return True

    def __lt__(self, other):
        for ind in range(len(self.numbers)):
            if self.numbers[ind] > other.numbers[ind]:
                return False
        return True

    def __len__(self):
        return len(self.numbers)

    def __getitem__(self, key):
        return self.numbers[key]

    def __str__(self):
        return str(self.numbers)


if __name__ == '__main__':
    a = Vector([1, 2, 3, 4, 5])
    b = Vector([2, 4, 6, 8, 10, 12])
    a + b
    print(a.numbers)

    a = Vector([1, 2, 3, 4, 5])
    a * 5
    print(a.numbers)

    a = Vector([1, 2, 3, 4, 5])
    b = Vector([2, 4, 6, 8, 10, 12])
    res = a.mult_scalar(b, 45)
    print(res)

    a = Vector([1, 2, 3, 4, 5])
    b = Vector([2, 4, 6, 8, 10, 12])
    print(a > b)
    print(a < b)

    print('a -> ', a)
    print('a[5] -> ', a[4])