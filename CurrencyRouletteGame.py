import random
from helper_functions import check_input_validation
import functools
import time
from forex_python.converter import CurrencyRates
import sys


def get_money_interval(amount):
    c = CurrencyRates()
    dollar_rate = c.get_rate('USD', 'ILS')
    return amount * dollar_rate


def get_guess_from_user(amount):
    input_from_user = input(
        f"what do you think is the value of the generated number from USD to ILS of {amount}$ ?")
    while not check_input_validation(input_from_user, 1, sys.maxsize):
        input_from_user = input("wrong input, what do you think is the value of the generated number from USD to "
                                f"ILS of {amount}$ ?: ")
    return float(input_from_user)


class CurrencyRouletteGame:
    def __init__(self, difficulty=1):
        self.difficulty = int(difficulty)

    def get_bounderies(self, res):
        return int(res) - (5 - self.difficulty), int(res) + (5 - self.difficulty)

    def play(self):
        amount = random.randint(1, 101)
        user_guess = get_guess_from_user(amount)
        res = get_money_interval(amount)
        deviation_min, deviation_max = self.get_bounderies(res)
        if deviation_min <= float(user_guess) <= deviation_max:
            print("You Won!")
        else:
            print("You lose")
