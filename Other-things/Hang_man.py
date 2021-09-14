import random


class Hangman:

    def __init__(self):
        print("======================")
        print("  Welcome to Hangman")
        print("   1)start  2)exit")
        print("======================")
        choice = input("input the number:")

        if choice == '1':
            self.start_game()
        elif choice == '2':
            exit()
        else:
            self.__init__()

    def start_game(self):
        answer_list = ['lotto', 'array', 'mango', 'start', 'buddy']
        answer = random.choice(answer_list)
        progress = ['?', '?', '?', '?', '?']
        cnt = 0

        while True:
            print()
            guess = input("Guess:")

            if guess in answer:
                print()
                print("{} is in Answer.".format(guess))
                print("now Progress:", self.show_progress(guess, answer, progress))

            elif guess not in answer:

                self.draw_hangman(cnt)
                cnt += 1
                print()
                print("%s is not in Answer." % guess)
                print("{} is not in Answer.".format(guess))
                print("now Progress:", self.show_progress(guess, answer, progress))

            if self.show_progress(guess, answer, progress) == answer:
                print()
                print("!!!Correct!!!")
                print("\n\n")
                self.__init__()

    def show_progress(self, guess, answer, progress):
        for i, j in enumerate(answer):
            if guess == j:
                progress[i] = guess
        return "".join(progress)

    def draw_hangman(self, cnt):
        if cnt == 0:
            print("==========")
            print("| ")
            print("| ")
            print("| ")
            print("| ")
            print("| ")
        elif cnt == 1:
            print("==========")
            print("|     |")
            print("|     O")
            print("| ")
            print("| ")
            print("| ")
        elif cnt == 2:
            print("==========")
            print("|     |")
            print("|     O")
            print("|    /")
            print("| ")
            print("| ")
        elif cnt == 3:
            print("==========")
            print("|     |")
            print("|     O")
            print("|    /|\ ")
            print("| ")
            print("| ")
        elif cnt == 4:
            print("==========")
            print("|     |")
            print("|     O")
            print("|    /|\ ")
            print("|    / ")
            print("| ")
        elif cnt == 5:
            print("==========")
            print("|     |")
            print("|     O")
            print("|    /|\ ")
            print("|    / \ ")
            print("| ")
            print("===============")
            print(" | GAME OVER |")
            print("===============")
            self.__init__()


Hangman()
