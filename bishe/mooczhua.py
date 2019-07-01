#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-5-7 下午2:31 
# @Author : ho-ho
# @Site :  
# @File : mooczhua.py 
# @Description: 
# -------------------------------------------------------------------------------------

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x800')  # 指定浏览器分辨率
chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars')   # 隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
#chrome_options.add_argument('headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失
driver=webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.icourse163.org/learn/SYSU-1002533004#/learn/forumindex")
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
    '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[1]/li/div/a[1]'))


def save(scontent):
    file = open('medical.txt', 'a+')
    for i in range(len(scontent)):
        sj = str(scontent[i]).replace('[', '').replace(']', '')
        sj = sj.replace("'", '') + '\n'
        if len(sj) > 10:
            file.write(sj)
    file.close()
    print("save successfully ", count)


scontent = []  # 总内容
count = 1  # 计数
# 第一页的子网页链接数
links = driver.find_elements_by_xpath(
    '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[1]/li/div/a')
# 遍历列表的循环，使程序可以逐一点击
for i in range(len(links)):
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
        '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[1]/li/div/a[1]'))
    links = driver.find_elements_by_xpath(
        '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[1]/li/div/a')
    link = links[i]  # 逐一将列表里的a标签赋给link
    url = link.get_attribute('href')  # 提取a标签内的链接
    driver.get(url)
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
        '//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[1]/div/div[1]/h3'))
    title = driver.find_element_by_xpath(
        '//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[1]/div/div[1]/h3').text
    content = driver.find_element_by_xpath(
        '//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[1]/div/div[2]').text
    if content != '':
        scontent.append(title + '\t' + content)
    else:
        scontent.append(title)
    driver.back()  # 后退，返回原始页面目录页
    sleep(3)  # 留出加载时间
save(scontent) #保存内容

print('第1页的问题数为:', len(links))

# 获取课程总页数
page = []
li = driver.find_elements_by_xpath(
    '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[2]/div/a')  # 页数链接
for x in li:
    page.append(x.text)
page = [i for i in page if i != '']
if len(page) == 0:
    print('该课程只有1页')
    save(scontent)
else:
    print('课程的页数为:' + page[-2])
    # 第二页到最后一页
    for i in range(int(page[-2]) - 1):
        sleep(1)
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
            '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[1]/li/div/a[1]'))
        driver.find_element_by_xpath('//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[2]/div/a[11]').click()  # 翻页
        #driver.find_element_by_css_selector("[class='zbtn znxt']").click()  # 翻页功能，类名不能有空格，有空格可取后边的部分
        sleep(3)

        links = driver.find_elements_by_xpath(
            '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[1]/li/div/a')  # 获取到所有a标签，组成一个列表
        length = len(links)  # 列表的长度，一共有多少个a标签
        print('第', i + 2, '页的问题数为:', length)
        count = count + 1
        '''if count < 3:
            scontent = []
            continue
        else:'''
        for j in range(length):  # 遍历列表的循环，使程序可以逐一点击
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
                '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[1]/li/div/a[1]'))
            links = driver.find_elements_by_xpath(
                '//*[@id="courseLearn-inner-box"]/div/div[7]/div/div[2]/div/div[1]/div[1]/li/div/a')  # 在每次循环内都重新获取a标签，组成列表
            link = links[j]
            url = link.get_attribute('href')  # 提取a标签内的链接，注意这里提取出来的链接是字符串
            driver.get(url)  # 不能用click，因为click点击字符串没用，直接用浏览器打开网址即可
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
                '//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[1]/div/div[1]/h3'))
            title = driver.find_element_by_xpath(
                '//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[1]/div/div[1]/h3').text
            content = driver.find_element_by_xpath(
                '//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[1]/div/div[2]').text
            # print('已定位到元素')
            if content != '':
                scontent.append(title + '\t' + content)
                # print(title+'\t'+content)
            else:
                scontent.append(title)
            sleep(1)
            driver.back()  # 后退，返回原始页面目录页
            sleep(2)  # 留出加载时间
        save(scontent)
        scontent = []

driver.close()
