# Задачи для Lesson_3

print("\nЗадача 1: Пользователь вводит два целых числа. Выведите большее из них\n")

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 > num2:
    print("Большее:", num1)
elif num1 < num2:
    print("Большее:", num2)
else:
    print("Эти числа равны!")



print("\nЗадача 2: Пользователь вводит целое число. Проверьте является ли оно четырёхзначным\n")

number = int(input("Введите любое целое число: "))

if abs(number) < 10000 and abs(number) > 999:
    print("Число четырёхзачное)")
else:
    print("Число нечетырёхзначное(")



print("\nЗадача 3: Вводятся 3 числа (стороны), проверить существует ли такой треугольник с такими сторонами\n")

A = int(input("Введите сторону A: "))
B = int(input("Введите сторону B: "))
C = int(input("Введите сторону C: "))

if A + B > C and B + C > A and A + C > B:
    print("Треугольник существует!")
else:
    print("Треугольника не существует!")



print("\nЗадача 4: Пользователь вводит время в часах. Вывести какое время суток (утро, день, ...)\n")

"""
    Замечание! 
    Утро:  с 5 до 11 включительно
    День:  с 12 до 17 включительно 
    Вечер: с 18 до 22 включительно 
    Ночь:  с 23 до 4 включительно
    В остальных случаях выведите строку 'Ошибка'.
"""

hour = int(input("Введите час: "))

if hour >= 5 and hour <= 11:
    print("Сейчас утро\n")

elif hour >= 12 and hour <= 17:
    print("Сейчас день\n")

elif hour >= 18 and hour <= 22:
    print("Сейчас вечер\n")

elif (hour >= 23 and hour <= 24) or (hour >= 0 and hour <= 4):
    print("Сейчас ночь\n")

else:
    print("ERROR: time entered incorrectly")



print("\nЗадача 5: Пользователь вводит номер дня недели. Если число от 1 до 5, то вывести 'Выходные', от 6 до 7 'Будни'\n")

day = int(input("Введите номеря дня недели: "))

if day >= 1 and day <= 5:
    print("Сейчас будни")

elif day == 6 or day == 7:
    print("Сейчас выходные")

else:
    print("ERROR: error entering the day of the week")



print("\nЗадача 6: Пользователь вводит целое число. Выведите его строку-описание вида 'знак чётность число' или 'ноль'\n")

Number = int(input("Введите целое число: "))

if Number > 0:

    print("Положительное", end = " ")

    if Number % 2 == 1:
        print("нечётное число")
    
    else:
        print("чётное число")

elif Number < 0:

    print("Отрицательное", end = " ")

    if Number % 2 == 1:
        print("нечётное число")
    
    else:
        print("чётное число")

else:
    print("Ноль")



print("\nЗадача 7: Шахматный конь. Описание задачи читать в коде программе.\n")

"""
    Шахматный конь ходит буквой "Г" - на две клетки по вертикали в любом направлении
    и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски, 
    определите, может ли конь попасть с первой клетки на вторую одним ходом.
    В случае, если хотя бы одно из введенных чисел не лежит в диапазоне от 1 до 8, выведите строку "Ошибка!".
"""

x1 = int(input("Координата коня x1: "))
y1 = int(input("Координата коня y1: "))
x2 = int(input("Координата коня x2: "))
y2 = int(input("Координата коня y2: "))

# разберёмся сначала с ходом по вертикали

if (x1 < 1 or x1 > 8) or (x2 < 1 and x2 > 8) or (y1 < 1 and y1 > 8) or (y2 < 1 and y2 > 8):
    print("ERROR: введены неправильно координаты\n")

elif abs(y1 - y2) == 2:

    if abs(x1 - x2) == 1:
        print("Конь сможет сделать ход!\n") 

    else:
        print("Конь не сможет сделать ход!\n")

elif abs(x1 - x2) == 2:

    if abs(y1 - y2) == 1:
        print("Конь сможет сделать ход!\n") 

    else:
        print("Конь не сможет сделать ход!\n")

else:
    print("Конь не сможет сделать ход!\n")


    





