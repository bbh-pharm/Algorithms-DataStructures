#bingo
import random

size=5
computer = [[0]*size for i in range(size)]
computer_check = [[0]*size for i in range(size)]
player = [[0]*size for i in range(size)]
player_check = [[0]*size for i in range(size)]

i=0
while i<size:
    j=0
    while j<size:
        r_num = random.randint(1,50)
        check=0
        k=0
        while k<size:
            m=0
            while m<size:
                if computer[k][m]==r_num:
                    check=1
                m+=1
            k+=1

        if check==0:
            computer[i][j]=r_num
            j+=1
    i+=1

i=0
while i<size:
    j=0
    while j<size:
        r_num = random.randint(1,50)
        check=0
        k=0
        while k<size:
            m=0
            while m<size:
                if player[k][m]==r_num:
                    check=1
                m+=1
            k+=1

        if check==0:
            player[i][j]=r_num
            j+=1
    i+=1

turn=1
win=-1

#start game
while True:
    print('[computer]')
    for i in range(size):
        for j in range(size):
            print(computer[i][j], end='\t')
        print()
    
    print('[player]')
    for i in range(size):
        for j in range(size):
            print(player[i][j], end='\t')
        print()

    if turn==1:
        print('computer turn')
        com_y=random.randint(0,size-1)
        com_x=random.randint(0,size-1)
        if computer_check[com_y][com_x]==0:
            i=0
            while i<size:
                j=0
                while j<size:
                    if player[i][j]==computer[com_y][com_x]:
                        player[i][j]='X'
                        player_check[i][j]=1
                    j+=1
                i+=1
            computer[com_y][com_x]='O'
            computer_check[com_y][com_x]=1
            turn=2
    elif turn==2:
        player_y=int(input('player index y: '))
        player_x=int(input('player index x: '))
        if player_check[player_y][player_x]==0:
            i=0
            while i<size:
                j=0
                while j<size:
                    if computer[i][j]==player[player_y][player_x]:
                        computer[i][j]='X'
                        computer_check[i][j]=1
                    j+=1
                i+=1
            player[player_y][player_x]='O'
            player_check[player_y][player_x]=1
            turn=1

    #win
    i=0
    while i<size:
        if computer_check[i][0]==1 and computer_check[i][1]==1 and computer_check[i][2]==1 and computer_check[i][3]==1 and computer_check[i][4]==1:
            win=1
        elif player_check[i][0]==1 and player_check[i][1]==1 and player_check[i][2]==1 and player_check[i][3]==1 and player_check[i][4]==1:
            win=2
        if computer_check[0][i]==1 and computer_check[1][i]==1 and computer_check[2][i]==1 and computer_check[3][i]==1 and computer_check[4][i]==1:
            win=1
        elif player_check[0][i]==1 and player_check[1][i]==1 and player_check[2][i]==1 and player_check[3][i]==1 and player_check[4][i]==1:
            win=2
        i+=1

    if computer_check[0][0]==1 and computer_check[1][1]==1 and computer_check[2][2]==1 and computer_check[3][3]==1 and computer_check[4][4]==1:
        win=1
    elif player_check[0][0]==1 and player_check[1][1]==1 and player_check[2][2]==1 and player_check[3][3]==1 and player_check[4][4]==1:
        win=2

    if computer_check[0][4]==1 and computer_check[1][3]==1 and computer_check[2][2]==1 and computer_check[3][1]==1 and computer_check[4][0]==1:
        win=1
    elif player_check[0][4]==1 and player_check[1][3]==1 and player_check[2][2]==1 and player_check[3][1]==1 and player_check[4][0]==1:
        win=2

    if win==1:
        print('computer win')
        break
    elif win==2:
        print('player win')
        break
