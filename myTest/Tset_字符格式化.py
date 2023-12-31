value = 12.34567
print(f"result: {value:{10}.{4}}")

"""
在Python 3中，{:.4f}和{:.4}都是用于格式化浮点数的字符串格式化选项1。
然而，它们之间有一个重要的区别。{:.4f}将浮点数格式化为小数点后四位的字符串，而{:.4}则将浮点数格式化为四位有效数字的字符串。
下面是一个例子，假设有一个浮点数x = 3.1415926。使用{:.4f}格式化选项，我们可以得到3.14161。使用{:.4}格式化选项，我们可以得到3.1421。
这两个格式化选项在不同的情况下可能会有所不同。例如，当浮点数的小数点后的位数超过四位时，{:.4f}将四舍五入到小数点后四位，而{:.4}将四舍五入到四位有效数字1。
此外，{:.4f}始终返回一个包含小数点的字符串，而{:.4}只在需要时才包含小数点1。
"""