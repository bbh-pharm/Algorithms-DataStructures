import random

class ScoreMng:
    omr = [1, 4, 3, 2, 2]       # right answer
    me = []                     # submitted answer

    cnt = 0                     # Number of correct
    score = 0                   # Score

    def check_me(self):
        for i in range(len(self.omr)):
            r_score=random.randint(1,5)
            self.me.append(r_score)

    def check_omr(self):
        print('[',end='')
        i=0
        while i<5:
            if self.omr[i]==self.me[i]:
                self.cnt+=1
                print('[o]',end='')
            else:
                print('[x]',end='')
            i+=1
        print(']')

    def run(self):
        self.check_me()
        print(self.omr)
        print(self.me)
        self.check_omr()
        print('Score :',self.cnt*20)
        
sm=ScoreMng()
sm.run()
