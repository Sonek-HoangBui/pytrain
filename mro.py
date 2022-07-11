class A(object):
    __name__ = "A"
    def method(self):
        print('A class method')
        print(super().__name__)

class B(object):
    __name__ = "B"
    def method(self):
        print('B class method')
        print(super().__name__)
        super().method()

class C(object):
    __name__ = "C"
    def method(self):
        print('C class method')
        super().method()

class X(A,B):
    __name__ = "X"
    def method(self):
        print('X class method')
        print(super().__name__)
        super().method()

class Y(A,B):
    __name__ = "Y"
    def method(self):
        print('Y class method')
        print(super().__name__)
        super().method()

class P(Y,C,X): #p, y, a
    __name__ = "P"
    def method(self):
        print('P class method')
        print(super().__name__)
        super().method()
# P, Y, C, X, A
p = P()
p.method()

# huyền: P, Y, A, B
# nguyệt: P, Y, A, B, C, X
# thơm: P, A, B
# ánh: P, Y, A, B, X, C
# hoàng: P, Y, A, B, C