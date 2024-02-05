from django.shortcuts import render, get_object_or_404

from pages.models import TeamInfo, Hello, Player, Stadium


def mainpage(request):
 return render(request, 'pages/mainpage.html')

def team(request):
 team_history = TeamInfo.objects.order_by('pub_date') # -뺐으니 오래된게 제일 먼저나옴
 context = {'team_history': team_history}
 return render(request, 'pages/team/team_info.html', context)

def hello(request):
 hello = Hello.objects.order_by('pub_date') # -뺐으니 오래된게 제일 먼저나옴
 context = {'hello': hello}
 return render(request, 'pages/team/team_info_hello.html', context)

def stadium(request):
 stadium = Stadium.objects.order_by('pub_date')
 context = {'stadium': stadium}
 return render(request, 'pages/team/team_info_stadium.html', context)

def player_detail(request, player_id):
 player_instance = get_object_or_404(Player, id=player_id)
 context = { 'player_instance': player_instance}
 return render(request, 'pages/player/player_detail.html', context)

def scout(request):
 player_instance = Player.objects.order_by('pub_date')
 context = { 'player_instance': player_instance}
 return render(request, 'pages/player/scout.html', context)

def pitcher(request):
 player_instance = Player.objects.order_by('pub_date')
 context = {'player_instance': player_instance}
 return render(request, 'pages/player/pitcher.html', context)

def batter(request):
 player_instance = Player.objects.order_by('pub_date')
 context = {'player_instance': player_instance}
 return render(request, 'pages/player/batter.html', context)

def coach(request):
 player_instance = Player.objects.order_by('pub_date')
 context = {'player_instance': player_instance}
 return render(request, 'pages/player/coach.html', context)