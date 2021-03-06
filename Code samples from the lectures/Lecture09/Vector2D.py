import math

class Vector2:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def Length(self):
        return math.sqrt(self.X * self.X + self.Y * self.Y)

    def __neg__(self):
        self.X = -self.X
        self.Y = -self.Y
        return self

    def __add__(self, other):
        self.X += other.X
        self.Y += other.Y
        return self

    def __sub__(self, other):
        self += (-other)
        return self

    def __mul__(self, k):
        self.X *= k
        self.Y *= k
        return self


    def __str__(self):
        return "(" + str(self.X) + "," + str(self.Y) + ")"

    @staticmethod
    def Zero():
        return Vector2(0.0, 0.0)

    @staticmethod
    def UnitX():
        return Vector2(1.0, 0.0)

    @staticmethod
    def UnitY():
        return Vector2(0.0, 1.0)

v = Vector2.UnitX() * 10.0 - Vector2.UnitY() * 2.0
print(str(v))
