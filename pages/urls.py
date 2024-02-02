from django.urls import path
from . import views

urlpatterns = [
 path('', views.mainpage),
 path('team/introduction', views.team),
 path('team/hello/', views.hello),
 path('player/scout', views.player),
 path('player/scout/<int:player_id>/', views.player_detail, name='detail'),
]