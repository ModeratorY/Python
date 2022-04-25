# Задачи для Lesson_6

print("\nЗадача 1: Создать список из 10 чётных чисел и вывести при помощи for\n")

numbers = list(range(2, 22, 2))

for index in range(len(numbers)):
    print("index =", index, "number =", numbers[index])



print("\nЗадача 2: Создать список из 5 элементов. Сделать срез от второго индекса до четвёртого\n")

all_types = []
all_types.append(input("Введите первый элемент списка: "))
all_types.append(input("Введите второй элемент списка: "))
all_types.append(input("Введите третий элемент списка: "))
all_types.append(input("Введите четвёртый элемент списка: "))
all_types.append(input("Введите пятый элемент списка: "))

print("\nСрез от 2 до 4 элемента включительно:", all_types[1:4])



print("\nЗадача 3: Cоздайте пустой список и добавьте в него 10 случайных чисел и выведите их\n")

from random import randint

numbers = []

for index in range(10):
    numbers.append(randint(1,10))

for index in range(len(numbers)):
    print(numbers[index], end = " ")



print("\n\nЗадача 4: Удалите все элементы из списка, созданного в задании 3\n")

for index in range(len(numbers)):
    numbers.pop()

print(numbers)



print("\nЗадача 5: Создайте список из введенной пользователем строки и удалите из него символы 'a', 'e', 'o' - латинские\n")

print("Введите что угодно:", end = '  ')
string = list(input())

for index in range(len(string)):

    if 'e' in string:
        string.remove("e")
   
    elif 'a' in string:
        string.remove("a")
    
    elif 'o' in string:
        string.remove("o")

print("Исправленная строка:", end = ' ')

for index in range(len(string)):
    print(string[index], end = '')



print("\n\nЗадача 6: Даны два списка. Удалите все элементы первого списка из второго \n")

ls_1 = [1, 3, 4, 5]
ls_2 = [4, 5, 6, 7]

for index in range(len(ls_1)):
    if ls_1[index] in ls_2:
        ls_2.remove(ls_1[index])

print("Второй список после удаления элементов:", ls_2)



print("\nЗадача 7: Создайте список из случайных чисел и найдите наибольший элемент в нем.\n")

numbers = []
Max = 0

for index in range(10):
    numbers.append(randint(1, 100))

for index in range(len(numbers)):
    if Max < numbers[index]:
        Max = numbers[index]

print("Список сгенерированных элементов", numbers)
print("Максимальный элемент:", Max)

        

print("\nЗадача 8: Найдите наименьший элемент в списке из задания 7\n")

Min = 999999

for index in range(len(numbers)):
    if Min > numbers[index]:
        Min = numbers[index]

print("Список сгенерированных элементов в задаче 7", numbers)
print("Минимальный элемент:", Min)



print("\nЗадача 9: Найдите сумму элементов списка из задания 7\n")

Sum = 0

for index in range(len(numbers)):
    Sum += numbers[index]

print("Сумма чисел из писка из задания 7:", Sum)



print("\nЗадача 10: Найдите среднее арифмитическое элементов списка из задания 7\n")

print("Среднее арифмитическое элементов списка из задания 7: %.2f" % (Sum / len(numbers)))



print("\nСложная задача 1: Создайте список из случайных чисел. Найдите количество локальных максимумов\n")
# Локальный максимум — это элемент, который больше любого из своих соседей

numbers = []
cnt = 0

for index in range(10):
    numbers.append(randint(1, 10))

print("Список сгенерированных чисел:", numbers)

if numbers[0] > numbers[1]: 
    cnt += 1

if numbers[len(numbers) - 1] > numbers[len(numbers) - 2]: 
    cnt += 1

for index in range(1, len(numbers) - 1):
    if numbers[index] > numbers[index + 1] and numbers[index] > numbers[index - 1]:
            cnt += 1

print("Количество локальньных максимумов:", cnt)


print("\nСложное задание 2: Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.\n")

numbers = []
cnt = 0 # счётчик повторяющихся цифр
Repeating_digit = 0 # повторяющаяся цифра

for index in range(20):
    numbers.append(randint(1,5))

for index in range(len(numbers)):

    if Repeating_digit != numbers[index] and cnt < numbers.count(numbers[index]):
    
        cnt = numbers.count(numbers[index])
        Repeating_digit = numbers[index]

print("Список сгенерированных чисел:", numbers)
print("Максимальное количество одинаковых элементов:", cnt)



print("\nСложное задание 3: Создайте список из случайных чисел. Найдите второй максимум\n")

numbers = []

Max_1 = 0
Max_2 = 0

for index in range(10):
    numbers.append(randint(1, 100))

for index in range(0, len(numbers)):
    if Max_1 < numbers[index]:
        Max_1 = numbers[index]

for index in range(len(numbers)):
    if Max_2 < numbers[index] and numbers[index] < Max_1:
        Max_2 = numbers[index]

print("Список сгенерированных чисел:", numbers)
print("Второй максимум списка:", Max_2)



print("\nСложное задание 4: Создайте список из случайных чисел. Найдите количество различных элементов в нем.\n")

numbers = []
numbers_no_repet = []

for index in range(10):
    numbers.append(randint(1, 10))

for index in range(len(numbers)):
    if not(numbers[index] in numbers_no_repet):
        numbers_no_repet.append(numbers[index])

print("Список сгенерированных чисел:", numbers)
print("Количество различных элементов в сгенерированном списке:", len(numbers_no_repet))
