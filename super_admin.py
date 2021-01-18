from user import User
from casino import Casino
import operator


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
        # а також відсортовує 'GameMachines' відповідно до наявної у них суми грошей
        if money > self.casino.money:
            print('There is not enough money in the casino')
            return 0
        elif money < 0:
            print('''You can't withdraw negative amount of cash!''')
            return 0
        elif not self.casino.game_machines:
            self.casino.money -= money
            self.money += money
        else:
            amount_needed = 0
            money_needed = money
            while amount_needed != money:
                money_needed = money_needed - amount_needed
                self.casino.game_machines = \
                    sorted(self.casino.game_machines, key=operator.attrgetter('money'), reverse=True)
                amount_needed += self.casino.game_machines[0].take_money(money_needed)

            self.casino.money -= money
            self.money += money
            print('You successfully withdraw: ' + str(money) + '$ from your casino')
            print('Money left in Casino: ' + str(self.casino.money))
            counter = 0
            for item in self.casino.game_machines:
                print('Money left in game machine № ' + str(counter) + ' : ' + str(item.money) + '$.')
                counter += 1

    def casino_add_money(self, money):
        # метод за допомогою якого 'SuperAdmin' може додати гроші до рахунку 'casino'
        if self.money < money:
            print('''You can't put in the casino money that you didn't have''')
        elif money < 0:
            print('''You can't put in the casino negative amount of money''')
        else:
            self.casino.money += money
            self.money -= money
            print('You put: ' + str(money) + '$ in the casino.')
            print('You have: ' + str(self.money) + '$ left.')

    def game_machine_add_money(self, money, index):
        # метод за допомогою якого 'SuperAdmin' може додати гроші до 'GameMachine' у  'casino'
        if self.money < money:
            print('''You can't put in the GameMachine money that you didn't have''')
        else:
            check = self.casino.game_machines[index].put_money(money)
            if check:
                print('You successfully put in: ' + str(money) + '$ at the Game machine №' + str(index))
                self.money -= money
                self.casino.money += money
            print('You have: ' + str(self.money) + '$ left.')

    def remove_game_machine(self, index):
        # метод який дозвляє 'SuperAdmin' видаляти 'GameMachine' з Casino та рівномірно розприділяти гроші
        # між тими 'GameMachine' які залишилися
        if index > len(self.casino.game_machines) - 1 or index < 0:
            print('''You can't remove the Game Machine that didn't exist!''')
        else:
            machine_money = self.casino.game_machines[index].money
            self.casino.game_machines.pop(index)
            if len(self.casino.game_machines) != 0:
                print('Game Machine №' + str(index) + ' successfully removed from ' + self.name + '.')
                machine_money = int(machine_money / len(self.casino.game_machines))
                for el in self.casino.game_machines:
                    el.money += machine_money
            else:
                print('You removed all Game Machines from your casino')
                print('Money left in casino: ' + str(self.casino.money) + '$.')
