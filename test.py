from user import User
from super_admin import SuperAdmin


# Створення екземпляру класу 'User'
cat = User('Kit', 200)
# Перевірка екземпляру класу 'User' на можливість грати в 'GameMachine'
cat.play(25)
# Перевірка екземпляру класу 'User' на можливість грати в 'GameMachine' якщо сумма наявних у нього коштів:
# 1 - менша аніж та, яку він хоче покласти у 'GameMachine'
cat.play(350)
# 2 - являється відємним числом
cat.play(-350)

print('\n')

# Створення екземпляру класу 'SuperAdmin'
sobaka = SuperAdmin('Dog', 50000)
# Створення власного 'casino' екземпляром класу 'SuperAdmin'
sobaka.create_casino('Dog House')
# Створення 'GameMachine' у власному 'casino' екземпляром класу 'SuperAdmin'
sobaka.create_game_machine(10000)
# Спроба створити 'GameMachine' і покласти у неї більшу суму ніж та яка наявна у 'SuperAdmin'
sobaka.create_game_machine(50000)
# Спроба створити 'GameMachine' і покласти у неї 'відємну суму' грошей
sobaka.create_game_machine(-50000)
# Створення ще однієї 'GameMachine' у власному 'casino' екземпляром класу 'SuperAdmin'
sobaka.create_game_machine(20000)
# Перевірка кількості 'GameMachine' у власному 'casino' екземпляром класу 'SuperAdmin'
sobaka.casino.get_machine_count
# Перевірка суми грошей наявних у власному 'casino' екземпляром класу 'SuperAdmin'
sobaka.casino.get_money
# Спроба 'SuperAdmin' зняти гроші з рахунку власного 'casino'
sobaka.withdraw_money(25000)
# Спроба 'SuperAdmin' зняти суму грошей з власного 'casino' яка перевищує кількість наявних у 'casino' коштів
sobaka.withdraw_money(25000)
# Спроба 'SuperAdmin' зняти суму грошей яка являється відємним числом з власного 'casino'
sobaka.withdraw_money(-25000)
# Спроба 'SuperAdmin' покласти гроші на рахунку власного 'casino'
sobaka.casino_add_money(10000)
# Спроба 'SuperAdmin' покласти суму грошей якої у нього немає на рахунку власного 'casino'
sobaka.casino_add_money(40000)
# Спроба 'SuperAdmin' покласти суму грошей яка являється відємним числом на рахунок власного 'casino'
sobaka.casino_add_money(-40000)
# Спроба 'SuperAdmin' покласти суму грошей в 'GameMachine' з індексом 0
sobaka.game_machine_add_money(1000, 0)
# Спроба 'SuperAdmin' покласти суму грошей в 'GameMachine' з індексом 1
sobaka.game_machine_add_money(4500, 1)
# Спроба 'SuperAdmin' покласти суму грошей якої у нього немає  в 'GameMachine' з індексом 0
sobaka.game_machine_add_money(122000, 0)
# Спроба 'SuperAdmin' покласти суму грошей яка являється відємним числом в 'GameMachine' з індексом 0
sobaka.game_machine_add_money(-122000, 0)
# 1-ша спроба 'SuperAdmin' покласти гроші в неіснуючий 'GameMachine'
sobaka.game_machine_add_money(2000, -3)
# 2-га спроба 'SuperAdmin' покласти гроші в неіснуючий 'GameMachine'
sobaka.game_machine_add_money(2000, 3)
# Спроба 'SuperAdmin' видалити 'GameMachine' з індексом 0 з власного 'casino'
sobaka.remove_game_machine(0)
# Спроба 'SuperAdmin' видалити 'GameMachine' з індексом 1(неіснуючу) з власного 'casino'
sobaka.remove_game_machine(1)

