from user import User
from casino import Casino


class SuperAdmin(User):

    def __init__(self, name, money):
        super().__init__(name, money)
        self.casino = Casino

    def create_casino(self, name):
        # метод за допомогою якого 'SuperAdmin' створює 'casino'
        self.casino = Casino(name)
        print("You've just created a casino " + str(self.casino.name))
        return self.casino

    def create_game_machine(self, money):
        # метод за допомогою якого 'SuperAdmin' добавляє 'GameMachine' в 'casino'
        if money > self.money:
            print('''You can't create Game Machine with larger amount of money that you have''')
        elif money < 0:
            print('''You can't put in the GameMachine negative amount of money''')
        else:
            self.casino.add_game_machine(money)
            self.money = self.money - money
            print('You just created GameMachine')
            print('You have: ' + str(self.money) + '$ left.')

    def withdraw_money(self, money):
        # метод за допомогою якого 'SuperAdmin' може зняти гроші з рахунку 'casino'
        self.money += self.casino.withdraw_money(money)
        print('You have: ' + str(self.money) + '$ left.')

    def casino_add_money(self, money):
        # метод за допомогою якого 'SuperAdmin' може додати гроші до рахунку 'casino'
        if self.money < money:
            print('''You can't put in the casino money that you didn't have''')
        elif money < 0:
            print('''You can't put in the casino negative amount of money''')
        else:
            self.casino.casino_add_money(money)
            self.money -= money
            print('You have: ' + str(self.money) + '$ left.')

    def game_machine_add_money(self, money, index):
        # метод за допомогою якого 'SuperAdmin' може додати гроші до 'GameMachine' у  'casino'
        if self.money < money:
            print('''You can't put in the GameMachine money that you didn't have''')
        elif money < 0:
            print('''You can't put in the GameMachine negative amount of money''')
        else:
            check = self.casino.game_machine_add_money(money, index)
            if check:
                print('You successfully put in: ' + str(money) + '$ at the Game machine №' + str(index))
                self.money -= money
            print('You have: ' + str(self.money) + '$ left.')

    def remove_game_machine(self, index):
        # метод який дозвляє 'SuperAdmin' видаляти 'GameMachine' з Casino та рівномірно розприділяти гроші
        # між 'GameMachine' які залишилися
        self.casino.remove_game_machine(index)


