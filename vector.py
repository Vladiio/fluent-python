from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return (c for c in (self.x, self.y))

    def __add__(self, another):
        return Vector(self.x + another.x, self.y + another.y)

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        return bool(self.x or self.y)

    def __eq__(self, other):
        return tuple(self) == tuple(other)
