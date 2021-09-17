import random

class MemoryGame:
    count = 0
    size = 10
    front = []
    back = []

    def set_game(self):
        num=1
        for i in range(10):
            self.back.append(0)
            if i%2==0 and i!=0:
                num+=1
            self.front.append(num)

    def shuffle_game(self):
        i=0
        while i<100:
            r_num=random.randint(1,9)
            temp=self.front[0]
            self.front[0]=self.front[r_num]
            self.front[r_num]=temp
            i+=1

    def run(self):
        self.set_game()
        self.shuffle_game()

        while True:
            print(self.front)
            print(self.back)
            
            if self.count==5:
                print('End')
                break

            idx1=int(input('index1 : '))
            idx2=int(input('index2 : '))

            if self.front[idx1] == self.front[idx2] and idx1!=idx2:
                self.back[idx1]=1
                self.back[idx2]=1
                self.count+=1


mg=MemoryGame()
mg.run()
