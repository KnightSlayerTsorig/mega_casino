from game_machine import GameMachine
from random import randint


class User:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def play(self, money, casino):
        # метод який симулює гру в game_machine
        if self.money <= 0:
            print('''You can't play without money''')
        elif money > self.money:
            print('You cannot bet more money than you have')
        elif money <= 0:
            print('You cannot bet a negative number')
        elif not casino.game_machines:
            print('''Sorry there isn't any Game Machine at this casino''')
        else:
            self.money = self.money - money
            self.money += GameMachine(
                casino.game_machines[randint(0, len(casino.game_machines) - 1)].money).play(money)


