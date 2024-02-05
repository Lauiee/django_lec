from django.urls import path
from . import views

urlpatterns = [
 path('', views.mainpage),
 path('team/introduction', views.team),
 path('team/hello/', views.hello),
 path('player/scout', views.scout),
 path('player/pitcher', views.pitcher),
 path('player/batter', views.batter),
 path('player/coach', views.coach),
 path('player/<int:player_id>/', views.player_detail, name='detail'),
 path('team/stadium', views.stadium),
]