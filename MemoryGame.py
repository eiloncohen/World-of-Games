import random
from helper_functions import check_input_validation
import functools
import time


def is_list_equal(l1, l2):
    # check if list1 equal to list2
    if functools.reduce(lambda x, y: x and y, map(lambda p, q: int(p) == int(q), l1, l2), True):
        return True
    else:
        return False


def temp_print(l1: list):
    print(l1, end="")
    time.sleep(0.7)
    print("\r", end="")
    print("now please enter your numbers: ")


class MemoryGame:
    def __init__(self, difficulty=1):
        self.difficulty = int(difficulty)

    def generate_sequence(self):
        new_cards_sequence = []
        for i in range(self.difficulty):
            new_cards_sequence.append(random.randint(1, 101))
        return new_cards_sequence

    def get_list_from_user(self):
        list_from_user = []
        for i in range(self.difficulty):
            number_choised_by_user = input("please enter number: ")
            while not check_input_validation(number_choised_by_user, 1, 101):
                number_choised_by_user = input("wrong input, please enter number: ")
            list_from_user.append(number_choised_by_user)
        return list_from_user

    def play(self):
        l1 = self.generate_sequence()
        temp_print(l1)
        l2 = self.get_list_from_user()
        if is_list_equal(l1, l2):
            print("You Won!")
        else:
            print("You lose")
