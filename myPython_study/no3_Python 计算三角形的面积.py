"""
https://www.runoob.com/python3/python3-area-triangle.html
"""
# 三边的长度（仅限于整数）
a = int(input("请输入a边的长度（整数）"))
b = int(input("请输入b边的长度（整数）"))
c = int(input("请输入c边的长度（整数）"))
if a + b > c and a + b > c and b + c > a:
    # 计算半周长
    mySum = (a + b + c) / 2
    area = (mySum * (mySum - a) * (mySum - b) * (mySum - c)) ** 0.5
    print(f'三角形的面积为：{area}')
