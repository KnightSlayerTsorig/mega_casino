from game_machine import GameMachine


class Casino:

    def __init__(self, name):
        self.name = name
        self.money = 0
        self.game_machines = []
        self.game_machines_money = []

    def add_game_machine(self, money):
        # метод який добавляє 'GameMachine' з певною суммою грошей в ній в 'casino'
        self.money += money
        self.game_machines.append(GameMachine(money))
        self.game_machines_money.append(money)

    def withdraw_money(self, money):
        # метод за допомогою якого 'SuperAdmin' може зняти гроші з рахунку 'casino'
        if money > self.money:
            print('There is not enough money in the casino')
            return 0
        elif money < 0:
            print('''You can't withdraw negative amount of cash!''')
            return 0
        else:
            if max(self.game_machines_money) > money:
                amount_left = max(self.game_machines_money) - money
                self.game_machines_money.remove(max(self.game_machines_money))
                self.game_machines_money.append(amount_left)
                self.money -= money
                return money
            else:
                counter = len(self.game_machines_money)
                amount_requested = 0

                while amount_requested < money:
                    amount_requested += max(self.game_machines_money)
                    self.game_machines_money.remove(max(self.game_machines_money))

                amount_left = amount_requested - money

                if amount_requested > 0:
                    self.game_machines_money.append(amount_left)

                self.money -= money

                while counter != len(self.game_machines_money):
                    self.game_machines_money.append(0)

                return money

    def casino_add_money(self, money):
        # метод за допомогою якого 'SuperAdmin' може додати гроші до рахунку 'casino'
        self.money += money

    def game_machine_add_money(self, money, index):
        # метод за допомогою якого 'SuperAdmin' може додати гроші до 'GameMachine' у  'casino'
        if index > len(self.game_machines) - 1 or index < 0:
            print('''You can't add money to the Game Machine that didn't exist!''')
            return False
        elif index < 0:
            print('''You can't add money to the Game Machine that didn't exist!''')
            return False
        else:
            if money < 0:
                print('''You can't add negative amount of money to the Game Machine''')
                return False
            else:
                self.money += money
                self.game_machines_money[index] += money
                return True

    def remove_game_machine(self, index):
        # метод який дозвляє 'SuperAdmin' видаляти 'GameMachine' з Casino та рівномірно розприділяти гроші
        # між 'GameMachine' які залишилися
        if index > len(self.game_machines) - 1 or index < 0:
            print('''You can't remove the Game Machine that didn't exist!''')
        else:
            self.game_machines.pop(index)
            print('Game Machine №' + str(index) + ' successfully removed from ' + self.name + '.')
            if self.game_machines_money[index] == 0:
                self.game_machines_money.pop(index)
            else:
                money_from_game_machine = int(self.game_machines_money[index] / len(self.game_machines))
                self.game_machines_money.pop(index)
                for el in self.game_machines_money:
                    el += money_from_game_machine


    @property
    def get_money(self):
        # геттер який дозволяє отримати загальний залишок грошей у 'casino'
        print(str(self.money) + '$ left in casino.')
        return self.money

    @property
    def get_machine_count(self):
        # геттер який дозволяє дізнатися кількість 'GameMachines' у 'casino'
        print(len(self.game_machines))
        return len(self.game_machines)
