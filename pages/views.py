from django.shortcuts import render

from pages.models import TeamInfo, Hello


def mainpage(request):
 return render(request, 'pages/mainpage.html')

def team(request):
 team_history = TeamInfo.objects.order_by('pub_date') # -뺐으니 오래된게 제일 먼저나옴
 context = {'team_history': team_history}
 return render(request, 'pages/team_info.html', context)

def hello(request):
 hello = Hello.objects.order_by('pub_date') # -뺐으니 오래된게 제일 먼저나옴
 context = {'hello': hello}
 return render(request, 'pages/team_info_hello.html', context)