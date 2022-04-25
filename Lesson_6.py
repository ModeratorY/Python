# СПИСКИ В PYTHON

"""
    Список - это непрерывная динамическая коллекция элементов.
    Каждому элементу списка присваивается порядковый номер - его индекс.
    Первый индекс равен нулю, второй - единице и так далее...
    Основные операции для работы со списками - это индексирование, срезы, добавление и удаление элементов,
    а также проверка на наличие элемента в последовательности.
"""

# Примеры создания списка

empty_list = []

numbers = [40, 20, 90, 11, 5] # список из чисел 

fuits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange'] # список из строковых переменных

fractions = [3,14, 2.72, 1.41, 1.73, 17.9] # список из дробных чисел

values = [3.14, 10, 'Hello', False, 'Python is the best'] # список из различных типов данных

list_of_list = [[2, 4, 0], [11, 2, 10], [0, 19, 27]] # список спика


# Индексирование

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
print("\nНулевой элемент списка:", fruits[0])
print("Первый элемент списка:", fruits[1])
print("Четвёртый элемент списка:", fruits[4], end = '\n\n')

''' Списки в Python являются изменяемым типом данных. Мы можем изменять содержимое каждой из ячеек '''

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
print("Список до изменения: ", fruits)
fruits[0] = 'Watermelon'
fruits[3] = 'Lemon'
print("Список после изменения: ", fruits, end = '\n\n')

''' Индексирование работает и в обратную сторону '''

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
print("-1-ый элемент списка:", fruits[-1])
print("-2-ой элемент списка:", fruits[-2])
print("-3-ий элемент списка:", fruits[-3])


print("\n==========================================\n")


# Создание списка с помощью list()

letters = list('ABCDEF')
numbers = list(range(10))
even_numbers = list(range(0, 10, 2))
print("Letters:", letters)
print("Numbers:", numbers)
print("Even numbers:", even_numbers)


print("\n==========================================\n")


# Длина списка

''' Функция len() возвращает длину любой итерируемой переменной, переменной, по которой можно запустить цикл '''

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
numbers = [40, 20, 10, 2000]
string = 'Hello World'
print("Длина списка fruits:", len(fruits))
print("Длина списка numbers:", len(numbers))
print("Длина строки string:", len(string))
print("Длина range(10):", len(range(10)))


print("\n==========================================\n")


# Срезы

'''
    Срезом называется некоторая подпоследовательность. 
    Принцип действия срезов очень прост: мы "отрезаем" кусок
    от исходной последовательности элемента, не меняя её при этом.
'''

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']

# переменная = итерируемая_переменная[начальный_индекс : конечный_индекс - 1 : длина_шага]
print("fruits[0:3]:", fruits[0:3])

# Если начальный индекс равен 0, то его можно опустить
print("fruits[:2]:", fruits[:2])
print("fruits[:3]:", fruits[:3])
print("fruits[:4]:", fruits[:4])
print("fruits[:5]:", fruits[:5], end = '\n\n')

# Если конечный индекс равен длине списка, то его тоже можно опустить
print("fruits[::]:", fruits[::])
print("fruits[:len(fruits)]:", fruits[:len(fruits)], end = '\n\n')

# разбираемся с диной шага
print("fruits[::2]:", fruits[::2])
print("fruits[::3]:", fruits[::3])
print("fruits[::-1]:", fruits[::-1])
print("fruits[4:2:-1]:", fruits[4:2:-1])


print("\n==========================================\n")


# Перебор значений по индексам и без

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']

print("Перебор значений:", end = ' ')
for fruit in fruits:
    print(fruit, end = ' ')

print("\nПеребор по индексам:", end = ' ')
for index in range(len(fruits)):
    print(fruits[index], end = ' ')


print("\n\n==========================================\n")


# Операция in

'''
    С помощью in мы можем проверить наличие элемента в списке, строке и любой другой итерируемой переменной.
'''

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']

if 'Apple' in fruits:
    print("В списке есть элемент Apple")

if 'Lemon' in fruits:
    print("в списке есть Lemon\n")
    
else:
    print("В списке нет Lemon\n")

# Более сложный пример

all_fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
my_favorite_fruits = ['Apple', 'Orange']

for item in all_fruits:
    if item in my_favorite_fruits:
        print(item + " is my favorite fruit")
    else:
        print(item + " isn't my favorite fruit")


print("\n==========================================\n")


# Методы для работы со списками

''' Начнем с метода append(), который добавляет элемент в конец списка '''

# создадим любой список
number = list(range(0,10,2))
# добавляем при помощи append() элемент в конец списка
number.append(200)
number.append(201)
number.append(202)
print("Cписок number:", number)

all_types = [1, 2.1, 'Hello!']
all_types.append(2022)
all_types.append('IV век')
all_types.append([1, 0, 1, 0])
print("Cписок all_types:", all_types, end = '\n\n')


'''  insert(), который добавляет элемент в список на произвольную позицию '''

numbers = list(range(10))
numbers.insert(0, 2021) # .insert(index, переменная)
numbers.insert(2, 'LMAO')
print("Список numbers после метода .insert():", numbers, end = '\n\n')


''' Метод pop() удаляет элемент из списка по его индексу '''

numbers = list(range(10))
print("Изначально:", numbers)
numbers.pop(0)
print("после .pop(0):", numbers)
numbers.pop(0)
print("после .pop(0):", numbers)
numbers.pop(2)
print("после .pop(2):", numbers)
# Чтобы удалить последний элемент, вызовем метод pop без аргументов
numbers.pop()
print("после .pop():", numbers)
numbers.pop()
print("после .pop():", numbers, end = '\n\n')


''' Метод remove() удаляет первый найденный по значению элемент в списке '''

all_types = [10, 'Python', 10, 3.14, 'Python', ['I', 'am', 'list']]
print("До remove():", all_types)
all_types.remove(3.14)
print("После remove(3.14):", all_types)
all_types.remove(10)
print("После remove(10):", all_types)
all_types.remove('Python')
print("После remove('Python'):", all_types, end = '\n\n')


''' Посчитать элементы списка можно с помощью метода count() '''

numbers = [100, 100, 100, 200, 200, 500, 500, 500, 500, 500, 999]

print("Значений 100 в списке:", numbers.count(100))
print("Значений 500 в списке:", numbers.count(500))
print("Значений 2000 в списке:", numbers.count(2000), end = '\n\n')


''' Метод sort() сортирует список по возрастанию значений его элементов '''

numbers = [100, 2, 11, 9, 3, 1024, 567, 78]
print("numbers до sort():", numbers)
numbers.sort()
print("numbers после sort():", numbers)

fruits = ['Orange', 'Grape', 'Peach', 'Banan', 'Apple']
print("fruits после sort():", fruits)
fruits.sort()
print("fruits после sort():", fruits)

# Мы можем изменять порядок сортировки с помощью параметра revers =
# По умолчанию этот параметр равен False

fruits = ['Orange', 'Grape', 'Peach', 'Banan', 'Apple']
fruits.sort(reverse = True)
print("fruits после sort(revers = True):", fruits, end = '\n\n')


''' Иногда нам нужно перевернуть список. Для этого есть метод reverse() '''

numbers = [100, 2, 11, 9, 3, 1024, 567, 78]
print("numbers до reverse():", numbers)
numbers.reverse()
print("numbers полсе reverse():", numbers)

fruits = ['Orange', 'Grape', 'Peach', 'Banan', 'Apple']
print("fruits до reverse():", fruits)
fruits.reverse()
print("fruits после reverse():", fruits, end = '\n\n')


''' Допустим, у нас есть два списка и нам нужно их объединить. Для этого есть полезный метод extend() '''

fruits = ['Banana', 'Apple', 'Grape']
vegetables = ['Tomato', 'Cucumber', 'Potato', 'Carrot']

# Список в конец которого запишется второй список . extend( Список который запишется в конец )
fruits.extend(vegetables)
print("fruits.extend(vegetables):", fruits, end = '\n\n')


''' В природе существует специальный метод для очистки списка — clear() '''

fruits = ['Banana', 'Apple', 'Grape']
print("До clear():", fruits)
fruits.clear()
print("После clear():", fruits, end = '\n\n')


''' Метод index() возвращает индекс элемента. '''

fruits = ['Banana', 'Apple', 'Grape']
print("Индекс 'Banana':", fruits.index('Banana'))
print("Индекс 'Apple': ", fruits.index('Apple'))
print("Индекс 'Grape': ", fruits.index('Grape'), end = '\n\n\n')


''' Метод copy() копирует список и возвращает его брата-близнеца. '''

# если мы просто присвоим уже существующий список новой переменной, то на первый взгляд всё выглядит неплохо:
fruits = ['Banana', 'Apple', 'Grape']
new_fruits = fruits

print("Список fruits:", fruits)
print("Список new_fruits:", new_fruits, end = '\n\n')

print("При простом присваивании:")
fruits.pop()
print("Список fruits:", fruits)
print("Список new_fruits:", new_fruits, end = '\n\n')

# При прямом присваивании списков копирования не происходит. Обе переменные начинают ссылаться на один и тот же список!
# Поэтому используем метод copy()

fruits = ['Banana', 'Apple', 'Grape']
new_fruits = fruits.copy()

print("При методе copy():")
fruits.pop()
print("Список fruits:", fruits)
print("Список new_fruits:", new_fruits, end = '\n\n')

