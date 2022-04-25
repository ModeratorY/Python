# Задачи для Lesson_7

from cmath import pi
from random import randint


print("\nЗадача 1: Напишите функцию, которая получает в качестве аргумента радиус круга и находит его площадь\n")

def Circle(radius):
    return pi * (radius ** 2)

print("Площадь круга с радиусом 4 = %.1f" % Circle(4))
print("Площадь круга с радиусом 15 = %.1f" % Circle(15))
print("Площадь круга с радиусом 34 = %.1f" % Circle(34))



print("\nЗадача 2: Напишите функцию, которая возвращает True, если число делится на 3, и False, если - нет\n")

def Div_by_three(arg):

    if arg % 3 == 0:
        return True

    else:
        return False


print("Число 324 делится на 3:", Div_by_three(324))
print("Число 6335 делится на 3:", Div_by_three(6335))
print("Число 42 делится на 3:", Div_by_three(42))
print("Число 90991 делится на 3:", Div_by_three(90991))



print("\nЗадача 3: Напишите функцию, которая возвращает максимальный элемент из переданного в нее списка.\n")

def Max_in_list(mylist):

    Max = -99999

    for index in range(len(mylist)):
        if Max < mylist[index]:
            Max = mylist[index]

    return Max


numbers = []

for index in range(10):
    numbers.append(randint(1, 1000))

print("Список сгенерированных чисел:", numbers)
print("Максимальный элемент в списке:", Max_in_list(numbers))



print("\nЗадача 4: Напишите функцию, которая возвращает количество чётных элементов в списке\n")

def Even_num(mylist):

    cnt = 0

    for index in range(len(mylist)):
        if mylist[index] % 2 == 0:
            cnt += 1
    
    return cnt

numbers = []

for index in range(10):
    numbers.append(randint(1, 1000))

print("Список сгенерированных чисел:", numbers)
print("Количество чётных элементов в списке:", Even_num(numbers))



print("\nЗадача 5: Напишите функцию, которая возвращает список с уникальными (неповторяющихся) элементам\n")

def Uniq_elem(mylist):

    newlist = []

    for index in range(len(mylist)):
        if not(mylist[index] in newlist):
            newlist.append(mylist[index])
    
    newlist.sort()
    return newlist

numbers = []

for index in range(20):
    numbers.append(randint(1,10))

print("Список сгенерированных чисел:", numbers)
print("Список из уникальных элементов:", Uniq_elem(numbers))







