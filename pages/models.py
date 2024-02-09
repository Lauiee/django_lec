from django.db import models


class TeamInfo(models.Model):
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')


class Hello(models.Model):
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')


class Player(models.Model):
    playerName = models.CharField(max_length=200)  # 선수 이름 저장
    playerPos = models.CharField(max_length=200)  # 선수 포지션 저장
    playerBackNum = models.IntegerField(default=0)  # 선수 등번호 저장
    # MEDIA_ROOT/uploads/ 경로로 파일 업로드
    PlayerImg = models.FileField(upload_to='Uploaded Files/%y/%m/%d/')  # 선수 사진 저장
    is_New = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')  # 저장된 시간


class Stadium(models.Model):
    stadiumIntroTitle = models.CharField(max_length=200)  # 소개 제목
    stadiumIntroContent = models.TextField()  # 소개 내용
    stadiumName = models.CharField(max_length=200)  # 구장 명
    stadiumAdd = models.CharField(max_length=200)  # 주소
    stadiumSeat = models.CharField(max_length=200)  # 좌석 수
    stadiumSize = models.CharField(max_length=200)  # 총 면적
    stadiumScale = models.CharField(max_length=200)  # 규모
    stadiumFence = models.CharField(max_length=200)  # 펜스
    stadiumPoint = models.CharField(max_length=200)  # 특징
    stadiumOfficeAdd = models.CharField(max_length=200)  # 사무실 주소
    pub_date = models.DateTimeField('date published')  # 저장된 시간


class Player_detail(models.Model):
    연도 = models.CharField(max_length=20)
    팀 = models.CharField(max_length=20)
    나이 = models.CharField(max_length=20)
    P = models.CharField(max_length=20)
    G = models.CharField(max_length=20)
    타석 = models.CharField(max_length=20)
    타수 = models.CharField(max_length=20)
    득점 = models.CharField(max_length=20)
    안타 = models.CharField(max_length=20)
    field_2타 = models.CharField(max_length=20, db_column='`2타`')
    field_3타 = models.CharField(max_length=20, db_column='`3타`')
    홈런 = models.CharField(max_length=20)
    루타 = models.CharField(max_length=20)
    타점 = models.CharField(max_length=20)
    도루 = models.CharField(max_length=20)
    도실 = models.CharField(max_length=20)
    볼넷 = models.CharField(max_length=20)
    사구 = models.CharField(max_length=20)
    고4 = models.CharField(max_length=20)
    삼진 = models.CharField(max_length=20)
    병살 = models.CharField(max_length=20)
    희타 = models.CharField(max_length=20)
    희비 = models.CharField(max_length=20)
    타율 = models.CharField(max_length=20)
    출루 = models.CharField(max_length=20)
    장타 = models.CharField(max_length=20)
    OPS = models.CharField(max_length=20)
    wOBA = models.CharField(max_length=20)
    wRC_plus = models.CharField(max_length=20)
    WAR_star = models.CharField(max_length=20)
    WPA = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.연도} - {self.팀} - {self.나이} - {self.P} - {self.G} - {self.타석} - {self.타수} - {self.득점} - {self.안타} - {self.field_2타} - {self.field_3타} - {self.홈런} - {self.루타} - {self.타점} - {self.도루} - {self.도실} - {self.볼넷} - {self.사구} - {self.고4} - {self.삼진} - {self.병살} - {self.희타} - {self.희비} - {self.타율} - {self.출루} - {self.장타} - {self.OPS} - {self.wOBA} - {self.wRC_plus} - {self.WAR_star} - {self.WPA}"
