import random
import pprint


print("""

Easy,
Задача-1
 квадраты элементов исходного списка""")

a = [3,5,11,2,7]
b = [i**2 for i in a]
print(f"Дано: {a}")
print(f"Квадраты: {b}")

print("""

Easy,
Задача-2
 фрукты, присутствующие в обоих исходных списках""")

a = ["яблоко","банан", "мандарин", "арбуз", "киви"]
b = ["апельсин","банан", "киви", "арбуз", "дыня"]
print(f"Дано: {a}")
print(f"Дано: {b}")
c = [i for i in a for j in b if i == j]
print(f"Общие элементы списков: {c}")

print("""

Easy,
Задача-3
 список из элементов исходного, удовлетворяющих следующим условиям
 кратен 3 + Элемент положительный + Элемент не кратен 4
 """)

a = [3,5,-11,4,9,12]
print(f"Дано: {a}")
b = [i for i in a if i % 3 == 0 and i > 0 and i % 4 != 0 ]
print(f"Полученный список с условиями: {b}")

print("""

Normal,
Задача-1
 2500-значное произвольное число записать в файл
 вывести самую длинную последовательность одинаковых цифр из файла
 """)

with open("2500num.txt", "w") as f:
    a = [str(random.randint(0, 9)) for i in range(2500)]
    f.write(''.join(a))
with open("2500num.txt", "r") as f:
    a = f.read()
    s = a[0]
    for i in range(1,len(a)):
        if a[i-1] == a[i]:
            s += a[i]
        else:
            s += ","+a[i]
    num_count = s.split(",")
    max_count = 0
    for i in num_count:
        if len(i) > max_count:
            max_count = len(i)
            digit = i

    print(f"Максимальная последовательность = {max_count}  ({digit})")

print("""

Normal,
Задача-2
 Сформировать квадратную матрицу, в каждой строке которой
  находится ровно один ноль на случайном месте 
  """)

#N = int(input("Введите размер массива"))
N = 5
matr = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(1, 100))
    matr.append(row)

for i in range(len(matr)):
    matr[i][random.randint(0, N-1)] = 0

pprint.pprint(matr)

print("""

HARD,
Задача-1
 Куб состоит из n^3 прозрачных и непрозрачных 0 или 1 значений
 найти координаты просветов  
  """)
N = 3
matr = []
coord = []

#Создаю трехмерный массив
for i in range(N):
    Y = []
    for j in range(N):
        Z = []
        for k in range(N):
            Z.append(1)
        Y.append(Z)
    matr.append(Y)

#Добавляю случайные просветы
for i in range(N):
    matr[random.randint(0, N-1)][random.randint(0, N-1)][random.randint(0, N-1)] = 0

#Ищу координаты просветов
for x in range(len(matr)):
    for y in range(len(matr[x])):
        for z in  range(len(matr[x][y])):
            if matr[x][y][z] == 0:
                coord.append([x,y,z])


print("Наш трехмерный массив")
pprint.pprint(matr)
print("Координаты просветов")
for i in range(len(coord)):
    print(f"X = {coord[i][0]} Y = {coord[i][1]} Z = {coord[i][2]}")

print("""

HARD,
Задача-2
 Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей  
  """)

pwd = []
pwd_set = set()
pwd_count = dict()
top = 10
top_iter = 0

with open("pwd.txt", "r") as f:
    for i in f.readlines():
        pwd_data = i.split(";")
        pwd += pwd_data[1].splitlines()
    pwd_set = set(pwd)

    for i in pwd_set:
        pwd_count.update({i:pwd.count(i)})

    pwd_sorted = sorted(pwd_count.items(), key=lambda x: x[1], reverse=True)
    print("Топ 10 повторяющихся паролей:")
    print("Кол-во |Пароль  ")
    for i in pwd_sorted:
         if top_iter <= top:
             print(f"{i[1]}     {i[0]} ")
             top_iter += 1
         else:
             break

    # print(f" count set {len(pwd_set)} count pwd {len(pwd)}")

print("""

HARD,
Задача-3
 создать квадратную матрицу этого размера и по спирали заполнить её числами  
  """)


N = 5 #Размерность
kN = 0
num = 1
matr = [[0]*N for i in range(N)]
matr[N//2][N//2] = N * N
for h in range(N // 2):
    for i in range(N-kN):
        matr[h][i+h] = num
        num += 1
    for i in range(h+1, N-h):
        matr[i][-h-1] = num
        num += 1
    for i in range(h+1, N-h):
        matr[-h-1][-i-1] = num
        num += 1
    for i in range(h+1, N-(h+1)):
        matr[-i-1][h] = num
        num += 1

    kN += 2

pprint.pprint(matr)