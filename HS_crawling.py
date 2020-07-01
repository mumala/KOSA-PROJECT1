from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from selenium import webdriver
import time
import re


def scroll_down(x):
    SCROLL_PAUSE_TIME = x
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        time.sleep(SCROLL_PAUSE_TIME)
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def link_clipper(x):
    return ( x['onclick'].split(',')[0].replace('javascript:goSoftwareDetailPage(', '').replace("'", "") )
# font_page[0]['onclick'].split(',')[0].replace('javascript:goSoftwareDetailPage(', '').replace("'", "")

def get_ttf_file():
    count_ = 0

    for x in name_list.values():
        driver.get(x)
        time.sleep(1)
        driver.find_element_by_class_name("_btn_bit").click()
        driver.implicitly_wait(1)
        try:
            driver.find_element_by_class_name("btn_buy_v2").click()
            driver.implicitly_wait(1)
            driver.find_element_by_id("downloadLink").click()
            driver.implicitly_wait(1)


            soup = BeautifulSoup(driver.page_source,'html.parser')
            font_name_ineng = soup.select('#downloaderAlert .text')
            fidx = font_name_ineng[0].text.index('(')
            name = font_name_ineng[0].text[:fidx-5]

            driver.find_element_by_class_name("btn_lydown").click()
            print("download{}th font".format(count_))

            f = open('directory_Name.txt', 'w')
            f.write(str(name)+"\n")
            f.close()
        except:
            driver.find_element_by_class_name("_btn_bit").click()
            driver.implicitly_wait(1)
            driver.find_element_by_class_name("btn_buy_v2").click()
            driver.implicitly_wait(1)
            driver.find_element_by_id("downloadLink").click()

            driver.implicitly_wait(1)
            driver.find_element_by_class_name("btn_lydown").click()
        time.sleep(3)


driver = webdriver.Chrome()
time.sleep(1)
driver.get("https://software.naver.com/search.nhn?query=%ED%8F%B0%ED%8A%B8")
time.sleep(2)

scroll_down(2)
time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
font_page = soup.select('dl.info ._list_item_anchor')
time.sleep(2)

name_list = {}
len(name_list)

for i in font_page:
    name_list[i.text] = "https://software.naver.com" + link_clipper(i)
time.sleep(2)

#
# f = open('font_list.txt', 'w')
# for idx,value in name_list.items():
#     f.write(str(idx) + " $ "+str(value)+"\n")
#
# f.close()

get_ttf_file()
