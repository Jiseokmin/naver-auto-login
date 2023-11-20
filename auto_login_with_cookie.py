#환경 설정 세팅
# selenium의 webdriver를 사용하기 위한 import
import time
import pyperclip
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try :
    driver = webdriver.Chrome()
    driver.get("https://www.naver.com/")

    # 네이버 로그인 페이지 이동 버튼 클릭
    move_login_page_button = driver.find_element(By .CSS_SELECTOR, ".MyView-module__link_login___HpHMW")
    move_login_page_button.click()

    time.sleep(2)

    driver.add_cookie({"name": "NID_SAUTO", "value": "538595040"})

    # id 및 pw 입력
    user_id = '아이디를 입력하세요'
    id = driver.find_element(By .CSS_SELECTOR, "#id")
    pyperclip.copy(user_id)
    id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    user_pw = '비밀번호를 입력하세요'
    pw = driver.find_element(By .CSS_SELECTOR, "#pw")
    pyperclip.copy(user_pw)
    pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 네이버 로그인 페이지 이동 버튼 클릭
    login_button = driver.find_element(by=By.ID, value ="log.login")
    login_button.click()

    time.sleep(3)
    
    while True :
        continue
finally :
    pass