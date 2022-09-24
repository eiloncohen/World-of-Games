import random
from helper_functions import check_input_validation


class GuessGame:
    def __init__(self, difficulty=1):
        self.difficulty = int(difficulty)
        self.secret = 0
        self.guess = 0

    def generate_number(self):
        self.secret = random.randint(1, self.difficulty + 1)

    def get_guess_from_user(self):
        self.guess = input("please guess a number from 1 to difficulty level")
        while not check_input_validation(self.guess, 1, self.difficulty + 1):
            self.guess = input("please guess a number from 1 to difficulty level")
        return self.guess

    def compare_results(self):
        if int(self.guess) == self.secret:
            return True
        else:
            return False

    def play(self):
        self.generate_number()
        self.get_guess_from_user()
        res = self.compare_results()
        if res:
            print("correct! you won!!")
        else:
            print("you lose :-(")

