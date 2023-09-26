import zipfile
import random
import time
import sys


class MyIterator:
    # 单位字符集合
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789@'
    min_digits = 0
    max_digits = 0

    def __init__(self, min_digits, max_digits):
        # 实例化对象时给出密码位数范围，一般4到10位
        if min_digits < max_digits:
            self.min_digits = min_digits
            self.max_digits = max_digits
        else:
            self.min_digits = max_digits
            self.max_digits = min_digits

    # 迭代器访问定义
    def __iter__(self):
        return self

    def __next__(self):
        rst = str()
        for item in range(0, random.randrange(self.min_digits, self.max_digits + 1)):
            rst += random.choice(MyIterator.letters)
        return rst


def extract():
    start_time = time.time()
    zfile = zipfile.ZipFile("海盗派测试分析：MFQ&PPDCS_.zip")
    for p in MyIterator(4, 10):
        try:
            zfile.extractall(path=".", pwd=str(p).encode('utf-8'))
            print("the password is {}".format(p))
            now_time = time.time()
            print("spend time is {}".format(now_time - start_time))
            sys.exit(0)
        except Exception as e:
            pass


if __name__ == '__main__':
    extract()
