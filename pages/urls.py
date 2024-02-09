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
 path('player/batter/<str:playerName>/', views.batter_player_detail, name='detail_bat'),
 path('player/pitcher/<str:playerName>/', views.pitcher_player_detail, name='detail_pit'),
 path('player/coach/<str:playerName>/', views.coach_player_detail, name='detail_coa'),
 path('team/stadium', views.stadium),
]