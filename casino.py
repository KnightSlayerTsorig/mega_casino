from game_machine import GameMachine


class Casino:

    def __init__(self, name):
        self.name = name
        self.money = 0
        self.game_machines = []

    def add_game_machine(self, money):
        # метод який добавляє 'GameMachine' з певною суммою грошей в ній в 'casino'
        # А також відсортовує 'GameMachines' відповідно до наявної у них суми грошей
        self.money += money
        self.game_machines.append(GameMachine(money))

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
