import time

from bs4 import BeautifulSoup
from selenium import webdriver

import settings


def log_in_amazon(driver):
    # ブラウザ立ち上げ
    driver.get(settings.Amazon_ADDRESS)
    time.sleep(2)
    # ログイン
    login_btn = driver.find_element_by_id('nav-link-accountList')
    login_btn.click()
    time.sleep(1)

    login_email = driver.find_element_by_id('ap_email')
    login_email.send_keys(settings.LogIn_ID)
    next_btn = driver.find_element_by_id('continue')
    next_btn.click()
    time.sleep(2)

    login_pass = driver.find_element_by_id('ap_password')
    login_pass.send_keys(settings.LogIn_PASS)
    login_btn = driver.find_element_by_id('signInSubmit')
    login_btn.click()

    # 携帯電話登録のページがでてくる場合は後でとする
    try:
        mobile_skip = driver.find_element_by_id('ap-account-fixup-phone-skip-link')
        mobile_skip.click()
    except:
        pass
    time.sleep(2)

def go_to_order_history(driver):
    # 注文履歴画面へ
    order_history = driver.find_element_by_id('nav-orders')
    order_history.click()
    time.sleep(2)

def get_order_info(driver):
    # beautifulsoup使用開始
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    # 注文日
    order_date_titles = soup.find('div', text='注文日')
    