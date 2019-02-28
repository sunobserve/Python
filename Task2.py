import math
import random

print("""Easy, 
Задача-1 """)

fruit_list = ["яблоко","банан", "киви", "арбуз", "топинамбур"]
column_width = max(len(i) for i in fruit_list)
for i in range(0,fruit_list.__len__()):
    print(f"{i + 1}. {fruit_list[i].rjust(column_width) }")

print("""
Easy, 
Задача-2 """)

a = [1, 2, 3, 4, 11, 5, 11, 5, 7, 9]
b = [4, 5, 6, 7, 8, 9, 10, 11]
print(f"дано: a = {a} b = {b} ")
for i in b:
     while i in a:
         a.remove(i)
print(f"результат: a = {a} ")



print("""
Easy, 
Задача-3 """)

a = [1, 2, 3, 4, 11, 5, 11, 5, 7, 9]
b = []
print(f"дано: a = {a} b = {b} ")
for i in a:
    if i % 2 == 0:
        b.append((i / 4))
    else:
        b.append((i * 2))
print(f"результат: b = {b} ")


print("""
Normal, 
Задача-1 """)

a = [2, -5, 8, 9, -25, 25, 4]
b = []
print(f"дано: a = {a} b = {b}")
for i in a:
    if i > 0:
        if (math.sqrt(i) % 1) == 0:
            b.append(int(math.sqrt(i)))
print(f"результат: b = {b} ")


print("""
Normal, 
Задача-2 """)
user_date = "17.11.2017"
print(f"дано: дата = {user_date} ")
a = {1:"первое",2:"второе",3:"третее",
     4:"четвертое",5:"пятое",6:"шестое",
     7:"седьмое",8:"восьмое",9:"девятое",
     10:"десятое",11:"одинннадцатое",
     12:"двенадцатое",13:"тринадцатое",
     14:"четырнадцатое",15:"пятнадцатое",
     16:"шестнадцатое",17:"семнадцатое",
     18:"восемнадцатое",19:"девятнадцатое",
     20:"двадцатое",30:"тридцатое"}
b = {2:"двадцать",3:"тридцать"}
c = {1:"января",2:"февраля",3:"марта",
     4:"апреля",5:"мая",6:"июня",
     7:"июля",8:"августа",9:"сентября",
     10:"октября",11:"ноября",12:"декабря",}

print("Результат:")
dt = user_date.split(".")
if int(dt[0]) in a.keys():
    print(f"{(a.get(int(dt[0]))).title()} {c.get(int(dt[1]))} {dt[2]} года")
else:
    dt1 = dt[0]
    print(f"{(b.get(int(dt1[0]))).title()} {a.get(int(dt1[1]))} {c.get(int(dt[1]))} {dt[2]} года")



print("""
Normal, 
Задача-3 """)
n = 21
a = []
print(f"дано: Длина массива случайных чисел от -100 до 100 = {n} ")
for i in range(n):
    a.append(random.randint(-100, 100))
print(f"Результат: {a}")


print("""
Hard, 
Задача-1 """)
#text = input("Введите текст для проверки:")
text = "Првоверяем текст на колличество Latinskih bukv N и колличество слов"
print(f"дано: текст введенный пользователем = {text} ")

a = text.split(" ")
print(f"Кол-во слов в тексте: {len(a)}")
a = ("".join(a))
latin_letter_count = 0
for i in a:
#    Тоже рабочий вариант:
#    if  97 <= ord(i.lower()) <= 122:
    if i.lower() in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        latin_letter_count += 1
print(f"Кол-во латинских букв в тексте: {latin_letter_count}")

print("""
Hard, 
Задача-2 """)
#text1 = input("Введите текст 1 для сравнения:")
#text2 = input("Введите текст 2 для сравнения:")
text1 = "Сравниваем 2 текста на Колличество общих слов"
text2 = "сравниваем в текстах колличество общих слов слов 2"
print(f"дано: текст1 введенный пользователем = {text1} ")
print(f"дано: текст2 введенный пользователем = {text2} ")

tx1 = set((text1.lower()).split(" "))
tx2 = set((text2.lower()).split(" "))
print(f"Общие слова в двух текстах введенных пользователем: {tx1.intersection(tx2)}")

print("""
EXTRA, 
Задача-0 
""")

recipe_omelette = {'Яйцо':3,'Молоко':100,'Бекон':200,'Помидор':2}
foodstaf = {'Яйцо':10,'Молоко':1000,'Помидор':1}
need_buy = dict()

for key in recipe_omelette:
    if key in foodstaf.keys():
        if recipe_omelette[key] > foodstaf[key]:
            need_buy.update({key:recipe_omelette[key] - foodstaf[key]})
    else:
        need_buy.update({key: recipe_omelette[key]})

print("Наш рецепт:")
for key in recipe_omelette.keys():
    print(f"{key} {recipe_omelette[key]}")
print("Наличие продуктов в холодильнике:")
for key in foodstaf.keys():
    print(f"{key} {foodstaf[key]}")
print("Необходимо докупить следующие продукты:")
for key in need_buy.keys():
    print(f"{key} {need_buy[key]}")
