"""
https://www.runoob.com/python3/python3-swap-variables.html
"""

# 方法一：使用中间变量
a0 = 0
b0 = 1
temp = a0
a0 = b0
b0 = temp
print(a0, b0)  # 1 0

# 方法二：直接交换
a1 = 1
b1 = 2
a1, b1 = b1, a1
print(a1, b1)  # 2 1


