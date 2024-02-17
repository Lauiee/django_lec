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
 path('schedule_result', views.schedule),
 path('comment/pit_create/<int:player_id>/', views.pit_comment_create, name='pit_comment_create'),
 path('comment/bat_create/<int:player_id>/', views.bat_comment_create, name='bat_comment_create'),
 path('comment/coa_create/<int:player_id>/', views.coa_comment_create, name='coa_comment_create'),
 path('comment/update/<int:comment_id>/<int:player_id>/<int:flag>', views.comment_update, name='comment_update'),
 path('comment/delete/<int:comment_id>/<int:player_id>/<int:flag>', views.comment_delete, name='comment_delete'),

]