# 네이버 자동로그인
  naver auto login program

- 개발 언어 - python (selenium, pyautogui)
- [ver#1] 9222 포트로 chrome 실행시켜 준 다음 실행
  1. cmd 실행 -> chrome.exe 파일 있는 경로로 이동 (64비트 기준)
     C:\Program Files\Google\Chrome\Application
  2. chrome.exe 파일 9222 포트로 디버깅 모드 실행
     chrome.exe --remote-debugging-port=9222 --user-data-dir="원하는 경로 및 폴더명 예시) C:/chrome_data"
  3. auto_login.py 코드 실행
  
- [ver#2] GUI로 ID, PW 값 받은 후 로그인 진행
  1. C 드라이브에 cookie 폴더 생성 및 cookie.txt 파일 생성
  2. cookie.txt 파일에 네이버 로그인창 -> F12 -> Application -> Cookies -> https://nid.naver.com -> NID_SAUTO 값 복붙 (해당 값이 있어야 2단계 인증 진행하지않음, 없다면 1회 로그인 후에 값 생성된것 확인하고 값 넣어주기)
  3. auto_login_with_cookie.py 코드 실행
  4. ID, PW 값 입력
