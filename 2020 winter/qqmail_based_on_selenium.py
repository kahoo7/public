#   -*- coding:utf-8 -*-
#   Program name: Selenium Practice #1
#   @author: kahoo from SCNU
#   Time: 2020 01 16 12:00

'''
    Readme.txt:
    This is a crawler written in selenium
    This program is used to log in QQ mailbox and get the number of messages in inbox and unread messages
'''

from selenium import webdriver
import time

if __name__ == '__main__':

        # 设置浏览器后台静默运行，并实例化浏览器对象，这里使用的是Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options = chrome_options)
    # url = 'https://mail.qq.com/'
    driver.get('https://mail.qq.com/')
    time.sleep(2) #等待浏览器渲染

        # 1，QQ邮箱页面：输入账号密码并登录邮箱
    qq_Account = input('plz enter your username: ')    # 输入账号
    qq_psw = input('plz enter your password: ')     # 输入密码

    #driver.find_element_by_xpath('//*[@id="qqLoginTab"]').click() 若预先登录了QQ会有快速登陆提示，需转到输入登录窗
    driver.switch_to.frame('login_frame')

    driver.find_element_by_xpath('//*[@id="u"]').send_keys(qq_Account)
    driver.find_element_by_xpath('//*[@id="p"]').send_keys(qq_psw)
    driver.find_element_by_xpath('//*[@id="login_button"]').click()
    time.sleep(2)

        # 2，查看收件箱，输出收件箱邮件的总数目及未读邮件数目
    driver.find_element_by_xpath('//*[@id="folder_1"]').click()
    driver.switch_to.frame('mainFrame')
    result = driver.find_element_by_xpath('//*[@id="qqmail_mailcontainer"]/div[1]').text
    print(result)


        # 关闭浏览器
    driver.close()
    driver.quit()