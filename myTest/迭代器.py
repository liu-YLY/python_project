"""
创建一个迭代器
1.一个类（对象）只要含有“__iter__”、"__next__"两个方法，就将其称为迭代器。
__iter__方法返回一个特殊的迭代器对象，而这个迭代器对象自动实现了_next__方法，
并返回一个值，最后通过抛出异常StopIteration来结束迭代。我们来给上一个例子增加__next__方法：

原文链接：https://blog.csdn.net/qq_45807032/article/details/105219674
"""
from collections import Iterable
from collections import Iterator


class Classmate(object):
    """定义一个同学类"""

    def __init__(self):
        self.name = list()
        self.name_num = 0

    def add(self, name):
        self.name.append(name)

    def __iter__(self):
        pass

    def __next__(self):
        pass


class1 = Classmate()
class1.add("张三")
class1.add("李四")
class1.add("王五")

print("判断是否是可迭代的对象：", isinstance(class1, Iterable))
print("判断是否是迭代器：", isinstance(class1, Iterator))

"""
可以发现，当需要读取的内容读取完之后不会停止，而是无限循环的继续返回空值。
因此我们可以为其添加抛出异常（StopIteration，python中用于标标识迭代完成，
防止出现无限循环的情况）的程序，当需要的数据读取完成时就抛出异常，从而结束：
"""

'''
from collections import Iterable
from collections import Iterator
import time
 
 
class Classmate(object):
    """定义一个同学类"""
 
    def __init__(self):
        self.name = list()
        self.name_num = 0
 
    def add(self,name):
        self.name.append(name)
    
    def __iter__(self):
        return self   # 返回本身
 
    def __next__(self):
       if self.name_num < len(self.name):
           ret = self.name[self.name_num]
           self.name_num += 1
           return ret
 
        # 抛出异常，当循环后自动结束
       else:
           raise StopIteration
 
 
class1 =  Classmate()
class1.add("张三")
class1.add("李四")
class1.add("王五")
 
print("判断是否是可迭代的对象：", isinstance(class1,Iterable))
 
print("判断是否是迭代器：", isinstance(class1,Iterator))
 
for name in class1:
    print(name)
    time.sleep(1)
 
'''