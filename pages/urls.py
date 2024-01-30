from django.urls import path
from . import views
urlpatterns = [
 path('', views.mainpage),
 path('team/introduction', views.team),
 path('team/hello/', views.hello),
]