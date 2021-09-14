#omok

import random

size = 10
omok = [[0]*size for i in range(size)]
turn = 0
win = 0

while True:
    #game print
    i=0
    while i<size:
        j=0
        while j<size:
            if omok[i][j]==0:
                print('+',end=' ')
            elif omok[i][j]==1:
                print('○',end=' ')
            elif omok[i][j]==2:
                print('●',end=' ')
            j+=1
        print()
        i+=1

    #computer turn
    if turn==0:
        print('computer turn')
        p1_y = random.randint(0,size-1)
        p1_x = random.randint(0,size-1)
        if omok[p1_y][p1_x]==0:
            omok[p1_y][p1_x]=1
            turn=1
    #player turn
    elif turn==1:
        print('player turn')
        p2_y = int(input('player index_y : '))
        p2_x = int(input('player index_x : '))
        if omok[p2_y][p2_x]==0:
            omok[p2_y][p2_x]=2
            turn=0

    #win
    i=0
    while i<size:
        j=0
        while j<size-4:
            
            if omok[i][j]==1 and omok[i][j+1]==1 and omok[i][j+2]==1 and omok[i][j+3]==1 and omok[i][j+4]==1:
                win=1
            elif omok[i][j]==2 and omok[i][j+1]==2 and omok[i][j+2]==2 and omok[i][j+3]==2 and omok[i][j+4]==2:
                win=2

            if omok[j][i]==1 and omok[j+1][i]==1 and omok[j+2][i]==1 and omok[j+3][i]==1 and omok[j+4][i]==1:
                win=1
            elif omok[j][i]==2 and omok[j+1][i]==2 and omok[j+2][i]==2 and omok[j+3][i]==2 and omok[j+4][i]==2:
                win=2
            j+=1
        i+=1

    i=0
    while i<size-4:
        j=0
        while j<size-4:
            if omok[i][j]==1 and omok[i+1][j+1]==1 and omok[i+2][j+2]==1 and omok[i+3][j+3]==1 and omok[i+4][j+4]==1:
                win=1
            elif omok[i][j]==2 and omok[i+1][j+1]==2 and omok[i+2][j+2]==2 and omok[i+3][j+3]==2 and omok[i+4][j+4]==2:
                win=2
            j+=1
        j=4
        while j<size:
            if omok[i][j]==1 and omok[i+1][j-1]==1 and omok[i+2][j-2]==1 and omok[i+3][j-3]==1 and omok[i+4][j-4]==1:
                win=1
            elif omok[i][j]==2 and omok[i+1][j-1]==2 and omok[i+2][j-2]==2 and omok[i+3][j-3]==2 and omok[i+4][j-4]==2:
                win=2
            j+=1
        i+=1

    if win==1:
        print('computer win')
        break
    elif win==2:
        print('player win')
        break
