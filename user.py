
from game_machine import GameMachine


class User:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def play(self, money):
        # метод який симулює гру в game_machine
        if self.money <= 0:
            print('''You can't play without money''')
        elif money > self.money:
            print('You cannot bet more money than you have')
        elif money <= 0:
            print('You cannot bet a negative number')
        else:
            self.money = self.money - money
            self.money += GameMachine(10000).play(money)


