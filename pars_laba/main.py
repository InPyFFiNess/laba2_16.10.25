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

chrome_version = random.randint(110, 140)
windows_version = random.randint(10, 11)
opts = Options()
opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT {windows_version}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=opts)

city_list = ['Баку', 'Екатеринбург', 'Санкт-Петербург', 'Барнаул', 'Грозный', 'Казань' , 'Калининград', 'Кемерово', 'Красноярск', 'Махачлкала', 'Минеральные Воды', 'Москва', 'Новокузнецк',
             'Ноябрьск', 'Омск', 'Самара', 'Сочи', 'Сургут', 'Томск', 'Тюмень', 'Уфа', 'Челябинкс', 'Ереван', 'Гомель', 'Кутаиси', 'Батуми', 'Тбилиси', 'Дели', 'Астана', 'Алматы',
             'Санья', 'Урумчи', 'Бишкек', 'Дубай', 'Паттайя', 'Туркменбаши', 'Стамбул', 'Ташкент', 'Хамбантота']

for item in city_list:

    driver.get('https://belavia.by/booking/#')

    from_county = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div:nth-child(1) > div > div > input')
    from_county.click()
    from_county.send_keys('Минск')
    driver.find_element(By.CLASS_NAME, value='label-D365g').click()

    to_city = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div.cell-iwglb.cell-1PZIX.cell_location-2RvhJ.cell_location-1cHks.cell_location_arrival-1bMPd > div > input')
    to_city.click()
    to_city.send_keys(item)
    labels = driver.find_elements(By.CLASS_NAME, 'label-D365g')
    for label in labels:
        if label.text == item:
            label.click()
            break

    date = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div.cell-iwglb.cell-1PZIX.cell_date-3b7Yk.cell_date-144rD > div > div > div > div > span.placeholder-3gtgX.placeholder-cZzDV')
    date.click()
    choose_date = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div.cell-iwglb.cell-1PZIX.cell_date-3b7Yk.cell_date-144rD > div > div.popup-15edQ.popup-3hNCz.popup_withoutTabs-arvWe > div.content-23l0u.content-24GD3 > div.block-1LKe3.block-1LKe3 > div > div > div:nth-child(1) > div.monthWrapper-1bC4p.monthWrapper-1bC4p.monthWrapper-1HcnT > div:nth-child(4) > div:nth-child(1)')
    choose_date.click()
    oneway = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.segments-2_MOj.segments-3Ho24.alternative-2JxWI > div > div > div > div.cell-iwglb.cell-1PZIX.cell_date-3b7Yk.cell_date-144rD > div > div.popup-15edQ.popup-3hNCz.popup_withoutTabs-arvWe > div.footer-IBTuW.footer-2myok > div > button.root-1LfbW.smallThird-3I8Kz.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-disableElevation.MuiButtonBase-root.footer__done-iXB30.footer__done-1oLEc.css-1cy74wo')
    oneway.click()

    find_button = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div > form > div:nth-child(1) > div.controls-2b-jA.controls-3txk3.controls_withCurrency-3KMFu > div.startSearch-S4Zt3.startSearch-Ufhdb.startSearch_iconMode-GEPyG.startSearch_iconMode-25Fjg.startSearch_withCurrency-2ePKS.startSearch_withCurrency-3T0fS > button')
    find_button.click()

    price = driver.find_element(By.CSS_SELECTOR, '#root > div.inner-1mUUA.inner__inner-377JM > div > div.inner-2BFYs.inner-1D6ql.results_withPromocodes-EQr4t > div.calendar-pJbfq > div.content-3uBrc > div > div > div.slider-yOS3h.slider-2n2Ba > div > div > div.dayWrapper-3RXmG.dayWrapper-3ITLw.dayWrapper_selected-1qSyX > div > div.price__wrapper-3WJKw.price__wrapper-5ilVX > span').text
    print(price)
