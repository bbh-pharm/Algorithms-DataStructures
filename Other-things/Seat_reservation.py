# 좌석 현황 출력 함수
def print_seat(seat):
    print("[MEGA MOVIE]")
    i=0
    while i<len(seat):
        if seat[i]==0:
            print('[ ]',end='')
        elif seat[i]==1:
            print('[o]',end='')
        i+=1
    print()

# 좌석 선택 함수
def select_seat(seat):
    print_seat(seat)

    idx=int(input('좌석 선택[1~7] : '))
    if seat[idx-1]==0:
        seat[idx-1]=1
    elif seat[idx-1]==1:
        print('이미 예매가 완료된 자리입니다.')

def tot(seat):
    count=0
    for i in seat:
        if i==1:
            count+=1
    return count*12000

def run():
    total=0
    seat=[0,0,0,0,0,0,0]
    while True:
        print("[1]예매하기")
        print("[2]종료하기")

        sel=int(input('메뉴 선택 : '))
        if sel==1:
            select_seat(seat)
        elif sel==2:
            result=tot(seat)
            print('총 매출액 :',result)
            break
run()

# ex127_문제.py
# 캐릭터의 위치 저장 함수
def set_player(game):
    player=0
    i=0
    while i<len(game):
        if game[i]==2:
            player=i
        i+=1
    return player

#이동 함수
def move(game,player):
    move=int(input('좌(1), 우(2) 입력 : '))
    if move==1:
        if player==0:
            print('이동 불가')
        else:
            game[player]=0
            game[player-1]=2
    elif move==2:
        if player==6:
            print('이동 불가')
        else:
            game[player]=0
            game[player+1]=2


# 실행 함수
def run():
     while True:
        print(game)
        player=set_player(game)
        move(game,player)

game=[0, 0, 2, 0, 0, 0, 0]
run()
