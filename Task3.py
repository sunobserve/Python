print("""

Easy,
Задача-1
 Ввод числа и точности округления""")
def get_dec(a):
    dec = []
    for i in range(len(a)):
        dec.append(int(a[i]) % 10)
    return dec
def get_str(a):
    s = ""
    for i in a:
        s = s + str(i)
    return s
def round_num(a,d):
    if float(a) % 1 == 0:
        return f"В числе {a} нет десятичной части"
    else:
        b = a.split(".")
        dec = get_dec(b[1])
        if len(dec) > int(d):
            if dec[int(d)] >= 5:
                dec[int(d)-1] = dec[int(d)-1]+1
                return b[0] + "." + get_str(dec[0:int(d)])
            else:
                return b[0] + "." + get_str(dec[0:int(d)])
        else:
            return a
a = input("Input number")
d = input("Input decimal")
print(round_num(a,d))

print("""

Easy,
Задача-2
Проверка билета счастливый или нет
""")
def check_ticket(a):
    val = [int(i) for i in a]
    if sum(val[:int(len(val)/2)]) ==  sum(val[int(len(val)/2):]):
        return "Счастливый"
    else:
        return "Не счастливый"
    return b

a = input("Введите номер билета")
print(check_ticket(a))

print("""

Normal,
Задача-1
вывод ряда Фибоначчи от n до m
""")
def F(n,m):
    fib = []
    a = 1
    b = 1
    if m <= 0 or n <= 0 or n > m:
        return "Не правильный интервал"
    elif n == 1 and m == 1:
        fib = [1]
    else:
        fib = [1,1]
        for i in range(m - 2):
            c = a + b
            a = b
            b = c
            fib.append(b)
    return fib[n-1:m]
print("Ряд Фибоначчи с n-элемента до m-элемента")
n = int(input("Введите n:"))
m = int(input("Введите m:"))
print(F(n,m))

print("""

Normal,
Задача-2
сортировка массива пузырьковым методом
""")

def sort_array(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
a = [21,34,51,2,3,7,99,14,17]
print("Сортировка массива")
print(f"Дано: {a}")
print(f"Сортировка: {sort_array(a)}")


print("""

HARD,
Задача-1
консольное меню
""")

database = []

def add():
    global database
    data = input("Введите целое число:")
    while True:
        if data.isdigit():
            database.append(int(data))
            break
        else:
            print("Ошибка ввода ")
            data = input("Введите целое число:")

def print_data():
    global database
    if len(database) == 0:
        print("Нет данных")
    else:
        print(database)

def print_menu(menu):
    for i, m in enumerate(menu, start=1):
        print(f"{i}. {m}")


def get_command(menu):
    command = int(input("Input commmand: "))

    if 1 <= command <= len(menu):
        return command
    else:
        return -1

def sum_data():
    global database
    if len(database) == 0:
        print("Нет данных")
    else:
        print(f"Сумма элементов масива равна: {sum(database)}")

def delete():
    global database
    if len(database) == 0:
        print("Нет данных")
    else:
        L = len(database)
        database = []
        print(f"Удалено {L} элементов")

menu = ["Добавить", "Распечатать", "Посчитать", "Удалить", "Выйти"]
commands = [add, print_data, sum_data , delete, exit]

while True:
    print_menu(menu)
    command = get_command(menu)

    if command == -1:
        print("Wrong command!")
        continue

    commands[command - 1]()








