import mysql.connector
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from pages.forms import CommentForm
from pages.models import TeamInfo, Hello, Player, Stadium, Comment


def mainpage(request):
    return render(request, 'pages/mainpage.html')

def schedule(request):
    try:
        # MySQL 연결
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3042",
            database="schedule"
        )

        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # 쿼리 실행
        cursor.execute("SELECT day, time, play, park FROM match2024_schedule")

        # 결과 가져오기
        schedules = cursor.fetchall()

        # 연결 종료
        cursor.close()
        conn.close()
    except Exception as e:
        # 오류가 발생했을 때 처리할 코드
        # 예를 들어 로깅하거나 사용자에게 오류 메시지를 보여줄 수 있습니다.
        schedules = None

    return render(request, 'pages/schedule/schedule_result.html', {'schedules': schedules})

def team(request):
    team_history = TeamInfo.objects.order_by('pub_date')  # -뺐으니 오래된게 제일 먼저나옴
    context = {'team_history': team_history}
    return render(request, 'pages/team/team_info.html', context)


def hello(request):
    hello = Hello.objects.order_by('pub_date')  # -뺐으니 오래된게 제일 먼저나옴
    context = {'hello': hello}
    return render(request, 'pages/team/team_info_hello.html', context)


def stadium(request):
    stadium = Stadium.objects.order_by('pub_date')
    context = {'stadium': stadium}
    return render(request, 'pages/team/team_info_stadium.html', context)


def scout(request):
    player_instance = Player.objects.order_by('pub_date')
    context = {'player_instance': player_instance}
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


def batter_player_detail(request, playerName):
    try:
        # MySQL 데이터베이스 연결 설정
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3042",
            database="batter"
        )

        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # player_name을 이용하여 적절한 쿼리 작성
        query = f"SELECT * FROM {playerName};"

        cursor.execute(query)
        player_data = cursor.fetchall()

        conn.commit()

        player_instance = get_object_or_404(Player, playerName=playerName)

        # 데이터를 템플릿에 전달
        return render(request, 'pages/player/batter_player_detail.html', {'player_data': player_data, 'player_instance': player_instance})
    except Exception as e:
        # 오류 발생 시 예외 처리
        print(f"Error fetching player data: {e}")
        return render(request, 'player_not_found.html')
    finally:
        # 연결 종료
        if conn:
            conn.close()


def pitcher_player_detail(request, playerName):
    try:
        # MySQL 데이터베이스 연결 설정
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3042",
            database="pitcher"
        )

        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # player_name을 이용하여 적절한 쿼리 작성
        query = f"SELECT * FROM {playerName};"

        cursor.execute(query)
        player_data = cursor.fetchall()

        conn.commit()

        player_instance = get_object_or_404(Player, playerName=playerName)

        # 데이터를 템플릿에 전달
        return render(request, 'pages/player/pitcher_player_detail.html', {'player_data': player_data, 'player_instance': player_instance})
    except Exception as e:
        # 오류 발생 시 예외 처리
        print(f"Error fetching player data: {e}")
        return render(request, 'player_not_found.html')
    finally:
        # 연결 종료
        if conn:
            conn.close()


def coach_player_detail(request, playerName):
    try:
        # MySQL 데이터베이스 연결 설정
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3042",
            database="coach"
        )

        # 데이터베이스 커서 생성
        cursor = conn.cursor()

        # player_name을 이용하여 적절한 쿼리 작성
        query = f"SELECT * FROM {playerName};"

        cursor.execute(query)
        player_data = cursor.fetchall()

        conn.commit()

        player_instance = get_object_or_404(Player, playerName=playerName)

        # 데이터를 템플릿에 전달
        return render(request, 'pages/player/coach_player_detail.html', {'player_data': player_data, 'player_instance': player_instance})
    except Exception as e:
        # 오류 발생 시 예외 처리
        print(f"Error fetching player data: {e}")
        return render(request, 'player_not_found.html')
    finally:
        # 연결 종료
        if conn:
            conn.close()

@login_required(login_url='accounts:login')
def pit_comment_create(request, player_id):

 player_instance = get_object_or_404(Player, pk=player_id)

 if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.content_list = player_instance
        comment.author = request.user
        comment.save()
        return redirect('detail_pit', playerName=player_instance.playerName)
 else:
    form = CommentForm()
 context = {'content_list': player_instance, 'form': form}
 return (render(request, 'pages/player/pitcher_player_detail.html', context))

@login_required(login_url='accounts:login')
def bat_comment_create(request, player_id):

 player_instance = get_object_or_404(Player, pk=player_id)

 if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.content_list = player_instance
        comment.author = request.user
        comment.save()
        return redirect('detail_bat', playerName=player_instance.playerName)
 else:
    form = CommentForm()
 context = {'content_list': player_instance, 'form': form}
 return (render(request, 'pages/player/batter_player_detail.html', context))


@login_required(login_url='accounts:login')
def coa_comment_create(request, player_id):

 player_instance = get_object_or_404(Player, pk=player_id)

 if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.content_list = player_instance
        comment.author = request.user
        comment.save()
        return redirect('detail_coa', playerName=player_instance.playerName)
 else:
    form = CommentForm()
 context = {'content_list': player_instance, 'form': form}
 return render(request, 'pages/player/coach_player_detail.html', context)

@login_required(login_url='accounts:login')
def comment_update(request, comment_id, player_id, flag):
 comment = get_object_or_404(Comment, pk=comment_id)
 player_instance = get_object_or_404(Player, pk=player_id)

 if request.user != comment.author:
     raise PermissionDenied
 if request.method == 'POST':
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        if flag == 1:
            return redirect('detail_pit', playerName=player_instance.playerName)
        elif flag == 2:
            return redirect('detail_bat', playerName=player_instance.playerName)
        else :
            return redirect('detail_coa', playerName=player_instance.playerName)

 else:
      form = CommentForm(instance=comment)

 context = {'comment': comment, 'form': form, 'player_id': player_id, 'flag': flag}
 return render(request, 'pages/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id, player_id, flag):
 comment = get_object_or_404(Comment, pk=comment_id)
 player_instance = get_object_or_404(Player, pk=player_id)

 if request.user != comment.author:
    raise PermissionDenied
 else:
    comment.delete()

    if flag==1:
        return redirect('detail_pit', playerName=player_instance.playerName)
    elif flag==2:
        return redirect('detail_bat', playerName=player_instance.playerName)
    elif flag==0:
        return redirect('detail_coa', playerName=player_instance.playerName)
    else :
        return redirect('/')