from django.contrib.auth.models import User
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

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Player, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
