"""
1、关于装饰器为什么要两层嵌套：https://segmentfault.com/q/1010000006990592
2、装饰器的理解：https://foofish.net/python-decorator.html
"""


# NO.1 一个简单的装饰器
def my_decorator(func):
    def wrapper():
        print("这是一个装饰器")
        func()

    return wrapper


@my_decorator
def say_hello():
    print("你好，世界！")


say_hello()
"""
这是一个装饰器
你好，世界！
"""


# NO.2 业务逻辑函数需要参数时
def my_decorator1(func):
    def wrapper(*args, **kwargs):
        print("这是一个装饰器")
        func(*args, **kwargs)

    return wrapper


@my_decorator1
def say_hello(name):
    print(f"你好，{name}！")


say_hello("张三")
"""
这是一个装饰器
你好，张三！
"""

# NO.3 带参数的装饰器
