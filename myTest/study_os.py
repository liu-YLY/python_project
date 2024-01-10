import os
# 模块学习网址：https://www.runoob.com/python3/python3-os-path.html
print(os.path.dirname(__file__))  # 返回文件夹路径：D:\python_project\myTest
print(os.path.dirname(os.path.dirname(__file__)))  # 返回上一级文件夹路径：D:\python_project

print(os.path.abspath(__file__))  # 返回绝对路径：D:\python_project\myTest\study_os.py

print(os.path.basename(__file__))  # 返回文件名：study_os.py

print(os.path.join(os.path.dirname(__file__), 'test.txt'))  # 拼接路径：D:\python_project\myTest\test.txt
print(os.path.join('base', 'test.txt'))  # 拼接路径：base\test.txt

print(os.path.split(os.path.abspath(__file__)))  # 把路径分割成 dirname 和 basename，返回一个元组：('D:\\python_project\\myTest', 'study_os.py')