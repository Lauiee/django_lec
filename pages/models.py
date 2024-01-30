from django.db import models
class TeamInfo(models.Model):
 subtitle = models.CharField(max_length=200)
 content = models.TextField()
 pub_date = models.DateTimeField('date published')

class Hello(models.Model):
 subtitle = models.CharField(max_length=200)
 content = models.TextField()
 pub_date = models.DateTimeField('date published')