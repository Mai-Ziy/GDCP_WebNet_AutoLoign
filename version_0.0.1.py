# coding = utf-8
import os
import time
import re
import requests
import pytesseract
from time import sleep
from selenium import webdriver
from PIL import Image,ImageEnhance
screenImg = screenImg = "E:/auto_xiaoyuanWEB/yanzhengma_png/yancode.png"#此处填写验证码截图存放路径
#第一层验证账号密码
username0 = "xxxxx"
password0 = "xxxxx"
#第二层验证账号密码
username1 = "xxxxx"
password1 = "xxxxx"

#下面句子需安装chromedriver
chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver) #模拟打开浏览器
#第一层URL随着区域不同而有所变化
driver.get("http://192.168.253.8/portal.do?wlanuserip=172.16.65.40&wlanacname=jtxy&url=http://detectportal.firefox.com/success.txt&rand=5da105a9") #打开网址
time.sleep(1)


driver.find_element_by_id('useridtemp').click()#点击用户名输入框
driver.find_element_by_id('useridtemp').send_keys(username0)#输入用户名

driver.find_element_by_id('passwd').click()#点击输入密码
driver.find_element_by_id('passwd').send_keys(password0)#输入密码

#driver.find_element_by_link_text('点击登录').click()#登录
driver.find_element_by_class_name("btnlogin").click()
time.sleep(1)
#driver.close()

driver.quit()#登录第一层完成，释放资源，关闭页面
#最大化窗口
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--kiosk')#进入chrome kiosk模式

driver = webdriver.Chrome(options = chrome_options)
#第二层登录URL
driver.get('http://enet.10000.gd.cn:10001/gz/index.jsp?wlanacip=183.36.229.1&wlanuserip=172.16.65.6')
time.sleep(1)


driver.find_element_by_id('username').click()#点击用户名输入框
driver.find_element_by_id('username').send_keys(username1)#输入用户名

driver.find_element_by_id('password').click()#点击输入密码
driver.find_element_by_id('password').send_keys(password1)#输入密码


driver.find_element_by_id('code').click()

#获取验证码图片(功能正常，截图完整)
a = driver.find_element_by_id("image_code")
#保存图像路径和命名
a.screenshot("E:/auto_xiaoyuanWEB/yanzhengma_png/yancode.png")
sleep(5)#等待线程（有闪硕bug）


#识别模块（功能缺失，识别率非常低）

#引入pytesseract识别图片中的验证码
#从文件读取截图，截取验证码位置再次保存
img = Image.open(screenImg)
img = img.convert('L') 			#转换模式：L | RGB
img = ImageEnhance.Contrast(img)#增强对比度
img = img.enhance(2.0) 			#增加饱和度
img.save(screenImg)


#再次读取识别验证码（功能缺失，识别率非常低）
img = Image.open(screenImg)
code = pytesseract.image_to_string(img)
#code= pytesser.image_file_to_string(screenImg)
driver.find_element_by_id("code").send_keys(code.strip())
yanzhengma = code.strip()
print(yanzhengma)#一定几率输出“空”
time.sleep(2)#给用户手动输入验证码一定时间

#退出程序，关闭浏览器，释放资源
driver.quit()


