# 第一道
"""
参考文档：
    Python 中的 type 和 isinstance
    https://www.freecodecamp.org/chinese/news/python-type-and-isinstance/
"""


class A(object):
    pass


class B(A):
    pass


print(isinstance(A(), A))
print(isinstance(B(), A))
print(type(A()) == A)
print(type(B()) == A)
'''
    True
    True
    True
    False
'''


# 第二道
class A:
    def get(self):
        self.say()

    def say(self):
        print('AAAAA')


class B(A):
    def say(self):
        print('BBBBB')


b = B()
b.get()
'''
    结果：BBBBB
    解释:
        当我们创建 b 对象并调用 b.get() 时，首先会执行 get 方法。
        在 get 方法中，调用了 say 方法。由于 B 类重写了 A 类的 say 方法，所以会执行 B 类的 say 方法，打印出 'BBBBB'。
'''
