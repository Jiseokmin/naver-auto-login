#환경 설정 세팅
# selenium의 webdriver를 사용하기 위한 import
import time
import pyperclip
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try :
    cookie_file_path = "C:\cookie\cookie.txt"
    
    with open(cookie_file_path, "r", encoding="utf-8") as file :
        cookie_value = file.read()
    
    uid = pyautogui.prompt('아이디를 입력하세요.')
    upid = pyautogui.password('패스워드를 입력하세요')

    driver = webdriver.Chrome()
    driver.get("https://www.naver.com/")

    # 네이버 로그인 페이지 이동 버튼 클릭
    move_login_page_button = driver.find_element(By .CSS_SELECTOR, ".MyView-module__link_login___HpHMW")
    move_login_page_button.click()

    time.sleep(2)

    driver.add_cookie({"name": "NID_SAUTO", "value": cookie_value})

    # id 및 pw 입력
    user_id = uid
    id = driver.find_element(By .CSS_SELECTOR, "#id")
    pyperclip.copy(user_id)
    id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    user_pw = upid
    pw = driver.find_element(By .CSS_SELECTOR, "#pw")
    pyperclip.copy(user_pw)
    pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 네이버 로그인 페이지 이동 버튼 클릭
    login_button = driver.find_element(by=By.ID, value ="log.login")
    login_button.click()

    time.sleep(3)

finally :
    pass