"""
from selenium import webdriver


# 1.创建Chrome或Firefox浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome()
# browser = webdriver.Firefox(executable_path ="D:\chromeDriver")

# 2.通过浏览器向服务器发送URL请求。如果能打开百度网站，说明安装成功。
browser.get("https://www.baidu.com/")
"""

"""
selenium在启动chrome时为了保证最快的运行效率，启动了一个裸浏览器，不带有任何插件和参数，需要手动配置参数
设置参数后，浏览器就不会自动关闭了

https://www.cnblogs.com/muxiaomu/p/16669022.html
在函数内执行的浏览器操作，在函数执行完毕之后，
程序内所有的步骤都结束了，关于这段程序的进程也就结束了，浏览器包含在内；
如果将浏览器全局后，打开浏览器不在函数内部，函数里面的程序执行完是不会关闭浏览器的。
"""
# https://blog.51cto.com/u_15949224/6039167
from selenium import webdriver

# 实例化浏览器
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

# 打开页面
url = 'https://www.baidu.com'
driver.get(url)
