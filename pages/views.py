import mysql.connector
from django.shortcuts import render, get_object_or_404

from pages.models import TeamInfo, Hello, Player, Stadium, Player_detail


def mainpage(request):
    return render(request, 'pages/mainpage.html')


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

        # 데이터를 템플릿에 전달
        return render(request, 'pages/player/batter_player_detail.html', {'player_data': player_data})
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

        # 데이터를 템플릿에 전달
        return render(request, 'pages/player/pitcher_player_detail.html', {'player_data': player_data})
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

        # 데이터를 템플릿에 전달
        return render(request, 'pages/player/coach_player_detail.html', {'player_data': player_data})
    except Exception as e:
        # 오류 발생 시 예외 처리
        print(f"Error fetching player data: {e}")
        return render(request, 'player_not_found.html')
    finally:
        # 연결 종료
        if conn:
            conn.close()
