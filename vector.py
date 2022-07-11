class Vector:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    def __str__(self) -> str:
        return 'Vector 1 (%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 0)
v2 = Vector(5, -2)
print(v1 + v2)