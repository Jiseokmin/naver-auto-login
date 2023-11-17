#환경 설정 세팅
# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬드라이버 실행
driver = webdriver.Chrome() 
driver.get('https://www.naver.com/')

time.sleep(3)

# 네이버 로그인 페이지 이동 버튼 클릭
move_login_page_button = driver.find_element(By .CSS_SELECTOR, ".MyView-module__link_login___HpHMW")
move_login_page_button.click()

time.sleep(2)

# id 및 pw 입력
id = driver.find_element(By .CSS_SELECTOR, "#id")
id.send_keys('test')

pw = driver.find_element(By .CSS_SELECTOR, "#pw")
pw.send_keys('tset')

time.sleep(2)

# 네이버 로그인 페이지 이동 버튼 클릭
login_button = driver.find_element(By .CSS_SELECTOR, ".btn_login")
login_button.click()

time.sleep(2)