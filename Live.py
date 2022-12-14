from helper_functions import check_input_validation
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame


def welcome(name: str):
    """
    param name: get the name of player
    return: the start menu sentence with this name inside
    """
    return f'''hello {name} and welcome to the World of Games (WoG)
Here toy can find many cool games to play'''


def load_game():
    """This function prints out the following text"""
    choose = input("""
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
    guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """)
    while not check_input_validation(choose, 1, 4):
        choose = input(""" 
    You choose wrong game number, please Please choose game to play: 
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
       guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """)
    difficulty = input("Please choose game difficulty from 1 to 5:")
    while not check_input_validation(difficulty, 1, 6):
        difficulty = input("You choose wrong difficulty, Please choose game difficulty from 1 to 5:")
    print(f"the  chosen game is: {choose}")
    print(f"the  difficulty  chosen is: {difficulty}")
    if choose == "1":
        game = MemoryGame(difficulty)
        game.play()
    if choose == "2":
        game = GuessGame(difficulty)
        game.play()
    if choose == "3":
        game = CurrencyRouletteGame(difficulty)
        game.play()
