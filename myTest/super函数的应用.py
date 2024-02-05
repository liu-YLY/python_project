"""
Python的super函数直观理解
https://zhuanlan.zhihu.com/p/356720970
"""

class A:
    def p(self):
        print('A')


class B(A):
    def p(self):
        super().p()
        print('B')


class C(B):
    def p(self):
        print('C')


class D(C):
    def p(self):
        print('D')


class E(C):
    def p(self):
        super().p()
        print('E')


class F(C):
    def p(self):
        super(C, self).p()
        print('F')


d = D()
d.p()  # D

e = E()
e.p()  # C  E

f = F()
f.p()  # A  B   F
