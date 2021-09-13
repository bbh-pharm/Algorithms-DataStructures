#tail_game
import random

size = 10
cnt=4
tail_game = [[0]*size for i in range(size)]
save_point = [[0,0] for i in range(cnt)]

r_y = random.randint(0, size-5)
r_x = random.randint(0, size-5)

i=1
while i<5:
    tail_game[r_y][r_x+i-1]=i
    i+=1

#item
for i in range(2):
    r_item_y = random.randint(0, size-1)
    r_item_x = random.randint(0, size-1)
    if tail_game[r_item_y][r_item_x] ==0:
        tail_game[r_item_y][r_item_x] = -5

while True:
    #save_point
    n=1
    while n<cnt+1:
        i=0
        while i<size:
            j=0
            while j<10:
                if tail_game[i][j] == n:
                    save_point[n-1][0]=i
                    save_point[n-1][1]=j
                    n+=1
                j+=1
            i+=1

    #game_print
    for i in tail_game:
        for j in i:
            if j==0:
                print('-',end=' ')
            elif j==1:
                print('◆',end =' ')
            elif j==-5:
                print('★',end =' ')
            else:
                print('◇',end =' ')
        print()

    #move
    move = int(input('1) left 2) right 3) up 4)down \nchoice : '))
    if move == 1:
        if r_x !=0 and tail_game[r_y][r_x-1] ==0:
            r_x-=1
            tail_game[r_y][r_x] = 1
            n=2
            for i in save_point:
                if i!=save_point[cnt-1]:
                    tail_game[i[0]][i[1]]=n
                    n+=1
                elif i==save_point[cnt-1]:
                    tail_game[i[0]][i[1]]=0
                    
        elif tail_game[r_y][r_x-1] == -5:
            r_x-=1
            tail_game[r_y][r_x] = 1
            n=2
            for i in save_point:
                tail_game[i[0]][i[1]]=n
                n+=1
            tail_y = save_point[cnt-1][0]
            tail_x = save_point[cnt-1][1]
            cnt+=1
            save_point.append([tail_y,tail_x])         
            
        else:
            print('can\'t move!')

    elif move == 2:
        if r_x!=size-1 and tail_game[r_y][r_x+1] == 0:
            r_x+=1
            tail_game[r_y][r_x] = 1
            n = 2
            for i in save_point:
                if i!=save_point[cnt-1]:
                    tail_game[i[0]][i[1]]=n
                    n+=1
                elif i==save_point[cnt-1]:
                    tail_game[i[0]][i[1]]=0
                    n+=1
                    
        elif tail_game[r_y][r_x+1] == -5:
            r_x+=1
            tail_game[r_y][r_x] = 1
            n=2
            for i in save_point:
                tail_game[i[0]][i[1]]=n
                n+=1
            tail_y = save_point[cnt-1][0]
            tail_x = save_point[cnt-1][1]
            cnt+=1
            save_point.append([tail_y,tail_x]) 
        
        else:
            print('can\'t move!') 

    elif move == 3:
        if r_y != 0 and tail_game[r_y-1][r_x] == 0:
            r_y -= 1
            tail_game[r_y][r_x] = 1
            n = 2
            for i in save_point:
                if i!=save_point[cnt-1]:
                    tail_game[i[0]][i[1]]=n
                    n+=1
                elif i==save_point[cnt-1]:
                    tail_game[i[0]][i[1]]=0

        elif tail_game[r_y-1][r_x] == -5:
            r_y-=1
            tail_game[r_y][r_x] = 1
            n=2
            for i in save_point:
                tail_game[i[0]][i[1]]=n
                n+=1
            tail_y = save_point[cnt-1][0]
            tail_x = save_point[cnt-1][1]
            cnt+=1
            save_point.append([tail_y,tail_x]) 
        
        else:
            print('can\'t move!')

    elif move == 4:
        if r_y != size-1 and tail_game[r_y+1][r_x] == 0:
            r_y +=1
            tail_game[r_y][r_x] = 1
            n = 2
            for i in save_point:
                if i!=save_point[cnt-1]:
                    tail_game[i[0]][i[1]]=n
                    n+=1
                elif i==save_point[cnt-1]:
                    tail_game[i[0]][i[1]]=0

        elif tail_game[r_y+1][r_x] == -5:
            r_y+=1
            tail_game[r_y][r_x] = 1
            n=2
            for i in save_point:
                tail_game[i[0]][i[1]]=n
                n+=1
            tail_y = save_point[cnt-1][0]
            tail_x = save_point[cnt-1][1]
            cnt+=1
            save_point.append([tail_y,tail_x]) 
        
        else:
            print('can\'t move!')
