import pandas
import mysql.connector
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

# MySQL 데이터베이스 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3042",
    database="batter"
)

# 데이터베이스 커서 생성
cursor = conn.cursor()

name = '서건창 '
encoded_name = quote(name)

# URL 조합
url = f"http://www.statiz.co.kr/player.php?opt=1&name={encoded_name}&birth=1989-08-22"

# URL 열기
html = urlopen(url)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# CSS 선택자를 사용하여 특정 클래스가 있는 div 태그를 찾음
table = soup.find('div', class_='box-body no-padding table-responsive')

# 테이블 데이터 추출
data = []
for row in table.find_all('tr')[2:]:  # 첫 번째 행은 헤더이므로 제외
    row_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
    data.append(row_data)

# 데이터프레임 생성
columns = ['연도', '팀', '나이', 'P', 'G', '타석', '타수', '득점',
           '안타', '2타', '3타', '홈런', '루타', '타점', '도루', '도실', '볼넷', '사구',
           '고4', '삼진', '병살', '희타', '희비', '타율', '출루',
           '장타', 'OPS', 'wOBA', 'wRC+', 'WAR*', 'WPA']  # 필요한 열 이름 정의
df = pandas.DataFrame(data, columns=columns)

# 테이블 생성 쿼리
create_table_query = f'''
CREATE TABLE {name} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    연도 VARCHAR(20),
    팀 VARCHAR(20),
    나이 VARCHAR(20),
    P VARCHAR(20),
    G VARCHAR(20),
    타석 VARCHAR(20),
    타수 VARCHAR(20),
    득점 VARCHAR(20),
    안타 VARCHAR(20),
    `2타` VARCHAR(20),
    `3타` VARCHAR(20),
    홈런 VARCHAR(20),
    루타 VARCHAR(20),
    타점 VARCHAR(20),
    도루 VARCHAR(20),
    도실 VARCHAR(20),
    볼넷 VARCHAR(20),
    사구 VARCHAR(20),
    고4 VARCHAR(20),
    삼진 VARCHAR(20),
    병살 VARCHAR(20),
    희타 VARCHAR(20),
    희비 VARCHAR(20),
    타율 VARCHAR(20),
    출루 VARCHAR(20),
    장타 VARCHAR(20),
    OPS VARCHAR(20),
    wOBA VARCHAR(20),
    wRC_plus VARCHAR(20),
    WAR_star VARCHAR(20),
    WPA VARCHAR(20)
);
'''

# 데이터 삽입 쿼리
insert_query = f"""INSERT INTO {name} (연도, 팀, 나이, P, G, 타석, 타수, 득점, 안타, `2타`, `3타`, 홈런, 루타, 타점, 도루, 도실, 볼넷, 사구, 고4, 삼진, 병살, 희타, 희비, 타율, 출루, 장타, OPS, wOBA, wRC_plus, WAR_star, WPA) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# 데이터프레임에서 값 추출하여 튜플로 변환
data_tuples = [tuple(x) for x in df.values]

# 쿼리 실행
cursor.execute(create_table_query)

# 데이터 삽입
cursor.executemany(insert_query, data_tuples)

# 변경사항 커밋
conn.commit()

# 연결 종료
conn.close()
