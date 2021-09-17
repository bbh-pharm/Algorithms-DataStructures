class Game:

    move = [0, 0, 0, 0, 8, 0, 0, 0, 0, 0]
    player = 0                            # player's position

    def set_player(self):
        for i in range(len(self.move)):
            if self.move[i]==8:
                self.player=i

    def print_game(self):
        for i in range(len(self.move)):
            if self.move[i]==0:
                print('[ ]',end=' ')
            else:
                print('읏',end=' ')
        print()

    def move_left(self):
        if self.player==0:
            print('you can\'t move on')
        else:
            self.move[self.player]=0
            self.player-=1
            self.move[self.player]=8

    def move_right(self):
        if self.player==9:
            print('you can\'t move on')
        else:
            self.move[self.player]=0
            self.player+=1
            self.move[self.player]=8

    def run(self):
        self.set_player()
        while True:
            self.print_game()
            choice=int(input('1) left 2) right 3)End'))
            if choice==1:
                self.move_left()
            elif choice==2:
                self.move_right()
            elif choice==3:
                print('end')
                break
game=Game()
game.run()
