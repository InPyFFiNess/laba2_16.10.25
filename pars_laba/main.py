from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
from concurrent.futures import ThreadPoolExecutor
import threading
import re
from selenium.webdriver.common.action_chains import ActionChains
import csv
import datetime
from functools import wraps
import os

LOG_FILE = 'log.csv'

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Дата', 'Время', 'Функция'])

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M:%S')
        func_name = func.__name__

        with open(LOG_FILE, mode='a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow([date_str, time_str, func_name])

        return func(*args, **kwargs)
    return wrapper

chrome_version = random.randint(110, 140)
windows_version = random.randint(10, 11)
opts = Options()
opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT {windows_version}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=opts)
actions = ActionChains(driver)

city_list = ['Баку', 'Екатеринбург', 'Санкт-Петербург', 'Барнаул', 'Грозный', 'Казань' , 'Калининград', 'Кемерово', 'Красноярск', 'Махачлкала', 'Минеральные Воды', 'Москва', 'Новокузнецк',
             'Ноябрьск', 'Омск', 'Самара', 'Сочи', 'Сургут', 'Томск', 'Тюмень', 'Уфа', 'Челябинкс', 'Ереван', 'Гомель', 'Кутаиси', 'Батуми', 'Тбилиси', 'Дели', 'Астана', 'Алматы',
             'Санья', 'Урумчи', 'Бишкек', 'Дубай', 'Паттайя', 'Туркменбаши', 'Стамбул', 'Ташкент', 'Хамбантота']

data = []

@log
def ToCity(city):
    to_city = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div.cell-iwglb.cell-1PZIX.cell_location-2RvhJ.cell_location-1cHks.cell_location_arrival-1bMPd > div > input')
    to_city.click()
    time.sleep(2)
    to_city.send_keys(city)
    labels = driver.find_elements(By.CLASS_NAME, 'label-D365g')
    time.sleep(3)
    for label in labels:
        if label.text == city:
            label.click()
            break
    time.sleep(2)

@log
def Date():
    date = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div.cell-iwglb.cell-1PZIX.cell_date-3b7Yk.cell_date-144rD > div > div > div > div > span.placeholder-3gtgX.placeholder-cZzDV')
    date.click()
    time.sleep(2)
    choose_date = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div.cell-iwglb.cell-1PZIX.cell_date-3b7Yk.cell_date-144rD > div > div.popup-15edQ.popup-3hNCz.popup_withoutTabs-arvWe > div.content-23l0u.content-24GD3 > div.block-1LKe3.block-1LKe3 > div > div > div:nth-child(1) > div.monthWrapper-1bC4p.monthWrapper-1bC4p.monthWrapper-1HcnT > div:nth-child(4) > div:nth-child(1)')
    choose_date.click()
    time.sleep(2)
    oneway = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div.cell-iwglb.cell-1PZIX.cell_date-3b7Yk.cell_date-144rD > div > div.popup-15edQ.popup-3hNCz.popup_withoutTabs-arvWe > div.footer-IBTuW.footer-2myok > div > button.root-1LfbW.smallThird-3I8Kz.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-disableElevation.MuiButtonBase-root.footer__done-iXB30.footer__done-1oLEc.css-1cy74wo')
    oneway.click()
    time.sleep(2)

@log
def FindButton():
    find_button = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.controls-2b-jA.controls-3txk3.controls_withCurrency-3KMFu > div.startSearch-S4Zt3.startSearch-Ufhdb.startSearch_iconMode-GEPyG.startSearch_iconMode-25Fjg.startSearch_withCurrency-2ePKS.startSearch_withCurrency-3T0fS > button')
    find_button.click()
    time.sleep(7)

@log
def Price(city):
    try:
        price = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div.inner-2BFYs.inner-1D6ql.results_withPromocodes-EQr4t > div.calendar-pJbfq > div.content-3uBrc > div > div > div.slider-yOS3h.slider-2n2Ba > div > div > div.dayWrapper-3RXmG.dayWrapper-3ITLw.dayWrapper_selected-1qSyX > div > div.price__wrapper-3WJKw.price__wrapper-5ilVX > span').text
    except:
        price = 'Рейса нет'
    data.append({
        "Город": city,
        "Цена": price
    })

driver.get('https://belavia.by/booking/#')
time.sleep(7)

from_county = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div:nth-child(1) > div > div > input')
from_county.click()
time.sleep(2)
from_county.send_keys('Минск')
driver.find_element(By.CLASS_NAME, value='label-D365g').click()
time.sleep(2)

ToCity(city_list[0])
Date()
FindButton()
Price(city_list[0])

for item in city_list[1:]:
    driver.get('https://belavia.by/booking/#')
    time.sleep(7)
    ToCity(item)
    FindButton()
    Price(item)

df = pd.DataFrame(data)
df.to_csv("info.csv", index=False, encoding="utf-8-sig")



