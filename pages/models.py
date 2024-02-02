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
  playerName = models.CharField(max_length=200) #선수 이름 저장
  playerPos = models.CharField(max_length=200) # 선수 포지션 저장
  playerBackNum = models.IntegerField(default=0)  # 선수 등번호 저장
  # MEDIA_ROOT/uploads/ 경로로 파일 업로드
  PlayerImg = models.FileField(upload_to='Uploaded Files/%y/%m/%d/') # 선수 사진 저장
  pub_date = models.DateTimeField('date published') # 저장된 시간