for i in range(2, 101):  # 左闭右开，[2,100]间的素数
    isTrue = False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            isTrue = False
            break
        else:
            isTrue = True
    if isTrue:
        print(i)

"""
# 输出指定范围内的素数
 
# take input from the user
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
 
for num in range(lower,upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
            
#  建议再加上一个说明避免在生产环境中使用for...else，因为其本身的歧义以及和try/finally...else完全相反的运作方式，
#  会影响可阅读性。具体可见《Effective Python》的Item 12
"""