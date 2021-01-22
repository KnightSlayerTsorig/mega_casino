from random import randint


class GameMachine:

    def __init__(self, money):
        self.money = money

    @property
    def show_money(self):
        # геттер, який отримує загальну сумму грошей у 'GameMachine'
        print(str(self.money) + ' left in the Game Machine')
        return self.money

    def take_money(self, amount):
        # метод, за допомогою якого 'SuperAdmin' може забрати гроші з 'GameMachine'
        if self.money - amount > 0:
            self.money = self.money - amount
            return amount
        else:
            amount = self.money
            self.money = 0
            return amount

    def put_money(self, amount):
        # метод, за допомогою якого 'SuperAdmin' може покласти гроші в 'GameMachine'
        if amount < 0:
            print('''You can't put in negative amount of money!''')
        else:
            self.money = self.money + amount
            print(str(self.money) + ' left in the Game Machine')
            return self.money

    def play(self, user_money):
        # метод який імітує поведінку слот машини
        if user_money < 0:
            print('''You can't put in negative amount of money!''')
        elif user_money * 3 > self.money:
            print('''There is not enough money at Game Machine''')
        else:
            self.money = self.money + user_money
            new_numbers = [randint(0, 9), randint(0, 9), randint(0, 9)]
            new_numbers_concat = ''.join([str(elem) for elem in new_numbers])
            counter = 0
            same_numbers = 0
            while counter < len(new_numbers) - 1:
                if new_numbers[counter] == new_numbers[counter + 1] or new_numbers[counter] == new_numbers[counter - 1]:
                    same_numbers += 1
                counter += 1
            print(new_numbers_concat)
            print(same_numbers)
            if same_numbers == 0:
                print('Sorry you loose :(')
                print(str(self.money) + ' left in the Game Machine')
                return 0
            elif same_numbers == 1:
                prize = user_money * 2
                self.money = self.money - prize
                print('Congrats you win ' + str(prize) + '$!')
                print(str(self.money) + ' left in the Game Machine')
                return prize
            elif same_numbers == 2:
                prize = user_money * 3
                self.money = self.money - prize
                print('Congrats you win ' + str(prize) + '$!')
                print(str(self.money) + ' left in the Game Machine')
                return prize

