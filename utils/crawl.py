import sys, os
#from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import urllib
import requests
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

webDriver = "chromedriver.exe"
page = 1

browser = webdriver.Chrome(webDriver)
html = browser.page_source
time.sleep(0.5)
action = ActionChains(browser)

purpose = ["Mainboard"] #["CPU", "GPU", "RAM"] or ["Mainboard"]
for category in purpose:
    file = 0
    while file < 300:
        if category == "Mainboard":
            url = f"http://search.danawa.com/dsearch.php?query=메인보드&page={page}"
            cls = ".prod_item.prod_item_top5"
        elif category == "CPU":
            url = f"http://search.danawa.com/dsearch.php?query=CPU&page={page}"
            cls = ".prod_item"
        elif category == "GPU":
            url = f"http://search.danawa.com/dsearch.php?query=그래픽카드&page={page}"
            cls = ".prod_item.prod_item_top5"
        elif category == "RAM":
            url = f"http://search.danawa.com/dsearch.php?query=RAM&page={page}"
            cls = ".prod_item"
        browser.get(url)

        ran = len(browser.find_elements(By.CSS_SELECTOR, ".product_list")[-1].find_elements(By.CSS_SELECTOR, cls))
        for i in range(ran):
            img = browser.find_elements(By.CSS_SELECTOR, ".product_list")[-1]
            img = img.find_elements(By.CSS_SELECTOR, cls)[i]

            if not img.get_attribute("id"): # 광고 이미지 스킵
                continue

            img = img.find_elements(By.TAG_NAME, 'img')[0]

            if (img.get_attribute('data-original')):
                img = "http:"+img.get_attribute('data-original')
            else:
                img = img.get_attribute('src')


            print(img)
            rep = img.split('/')
            length = rep[-1].index("shrink") + 7
            size = rep[-1][length:]
            rep[-1] = rep[-1].replace(size, "500:500")
            if category == "GPU":
                rep[-1] = rep[-1].replace("_1.", "_2.")
            zz = str(rep)[2:-2]
            newurl = zz.replace("', '", "/")
            browser.get(newurl)
            browser.find_element_by_tag_name("img").screenshot(f'HW/{category}/' + str(file) + '.jpg')
            print(str(file)+'.jpg')
            file+=1

            if file == 300: break

            browser.back()
        page+=1

