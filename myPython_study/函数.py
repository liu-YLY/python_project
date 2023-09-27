# https://www.runoob.com/python3/python3-function.html

"""

参数 *args, **kwargs 的使用示例

"""

def calc(*args, init_value, op, **kwargs):
    print(args, init_value, op, kwargs)


calc(1, 2, 3, init_value=0, op=2, x=4, y=5)


def calc1(*args, **kwargs):
    print(args, kwargs)


calc1(1, 2, 3, x=4, y=5, a=1)

print(calc)
