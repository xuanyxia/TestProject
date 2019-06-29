"""自动登陆首页注册的账号申请活动"""
from selenium import webdriver
from time import  sleep
import csv
driver=webdriver.Chrome()
driver.get("http://127.0.0.1/#/") #91wuli的网址
data_set = r'H:\register8.csv'
sleep(10)
reader = csv.reader(open(data_set,encoding='utf-8'))
rows = [row for row in reader]
print(rows)

for i in rows:
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/p[1]/i/a[1]/a').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/p[1]/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/p[1]/input').send_keys(i[0])
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/p[2]/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/p[2]/input').send_keys(i[1])
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/button[1]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/input').send_keys("香辣卤猪肉干肉")
    driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]/a').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/ul/li/p[3]').click()#免费试用
    sleep(1)
    element = driver.find_element_by_xpath("xxx")
    # driver.set_window_size(1000, 1200)
    # element_list = driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div/div[1]/p[5]/input[1]')
    # ActionChains(driver).move_to_element(element_list).perform()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[5]/div/div[2]/div/div[1]/p[5]/input[1]').click()#免费领取
    sleep(6)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[9]/div/div/button').click()#了解
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div/div[6]/div/input').send_keys('https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-21327572437.12.566f5f28hfQTvf&id=542247178064&scene=taobao_shop')
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div/div[6]/button').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div/div[9]/li[1]/label/span[1]/span').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div/div[9]/li[2]/label/span[1]/span').click()
    sleep(10)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div/div[2]/div/div[11]/button').click()
    sleep(2)
    driver.back()
driver.close()