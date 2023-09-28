"""
https://www.runoob.com/python3/python3-celsius-fahrenheit.html
"""

# 摄氏温度转华氏温度
userConsole = float(input("请选择：\n1、摄氏度转华氏温度\n2、华氏温度转摄氏度\n"))
if userConsole == 1:
    sheshidu = float(input("请输入摄氏温度："))
    print(f'{sheshidu}对应的华氏温度为：{(sheshidu * 1.8) + 32}')
elif userConsole == 2:
    huashidu = float(input("请输入华氏温度："))
    print(f'{huashidu}对应的摄氏温度为：{((huashidu - 32) / 1.8):{.2}f}')
    # 保留两位小数
else:
    print("请输入正确的序号")
