from selenium import webdriver
import time

# 启动浏览器
driver = webdriver.Chrome()  # 这里假设你使用的是Chrome浏览器，如果是其他浏览器，请下载对应的驱动并进行配置

# 打开网页
driver.get("https://chat.openai.com")  # 将URL替换为你要操作的网页地址

# 等待页面加载完成，可以根据实际情况调整等待时间
time.sleep(5)

# 查找文本域元素并获取其坐标
textarea_element = driver.find_element_by_id("prompt-textarea")  # 使用id属性找到文本域元素
textarea_box_x = textarea_element.location['x']  # 获取文本域的x坐标
textarea_box_y = textarea_element.location['y']  # 获取文本域的y坐标

# 输出文本域的坐标
print("文本域的坐标：", textarea_box_x, textarea_box_y)



