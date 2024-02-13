import pandas
import mysql.connector
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

# MySQL 데이터베이스 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3042",
    database="schedule"
)

# 데이터베이스 커서 생성
cursor = conn.cursor()

# 데이터베이스 커서 생성
cursor = conn.cursor()

# 쿼리 실행
cursor.execute("SELECT day, time, play, park FROM match_schedule")

# 결과 가져오기
schedules = cursor.fetchall()


print(schedules)
# 변경사항 커밋
conn.commit()

# 커넥션 닫기
conn.close()
