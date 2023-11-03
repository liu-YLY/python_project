"""
https://www.cnblogs.com/daniumiqi/p/12162192.html
"""


def funA(desA):
    print("It's funA")


def funB(desB):
    print("It's funB")
    print('---')
    print(desB)


@funB
@funA
def funC():
    print("It's funC")