#Задачи для Lesson_8

print("\nЗадача 1: Пользователь вводит имя, фамилия, возраст. Создайте словарь и запишите данные пользователя. Напечатайте словарь\n")

firstname = input("Введите своё имя: ")
lastname = input("Введите свою фамилию: ")
age = input("Введите свой возраст: ")

user = dict(firstname = firstname, lastname = lastname, age = age)

print(user)



print("\nЗадача 2: Выведите самое часто встречающееся слово в введенной строке.\n")

string = input("Введите любую строку: ")
list_of_words = string.split() # метод .split() разделяет строку на список строковых переменных

words = {}

for word in list_of_words:
    words[word] = words.get(word, 0) + 1

print("Часто встречающееся слово в строке:", max(words, key = words.get))



print("\nЗадача 3: Описание задачи смотреть в коде программы\n")

''' 
    Пользователь вводит число K - количество фруктов.
    Затем он вводит K фруктов в формате: название фрукта и его количество.
    Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.
    Выведите словарь.
'''

K = int(input("Введите число фруктов: "))
fruits = {}

for index in range(K):
    key = input("Введите фрукт: ")
    value = input("Введите его количество: ")
    fruits[key] = value

print(fruits)



print("\nЗадача 4: Описание задачи смотреть в коде программы\n")

''' 
    Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
    Создайте список friends и добавьте в него N словарей с ключами name и age.
    Найдите самого младшего из друзей и выведите его имя
'''

N = int(input("Введите количество друзей: "))
friends = []

for index in range(N):

    friend = dict()

    key = input("Введите имя друга: ")
    value = input("Введите возраст друга: ")

    friend[key] = value
    friends.append(friend)

print(friends)

Main_name = 'none'
Min_age = 1000

for friend in friends: # пробегаюсь по каждому словарю из списка
    for name in friend.keys(): # беру ключ из каждого списка
        if Min_age > int(friend[name]):
            Main_name = name
            Min_age = int(friend[name])

print("Самый младший друг:", Main_name)



print("\nЗадача 5: Описание задачи смотреть в коде программы\n")

'''
    Пользователь вводит число N. 
    Затем он вводит личные данные (имя и возраст) своих N друзей. 
    Создайте список friends и добавьте в него N словарей с ключами name и age.
    Выведите средний возраст всех друзей и самое длинное имя.
'''

N = int(input("Введите количество друзей: "))
friends = []

for index in range(N):

    friend = dict()

    key = input("Введите имя друга: ")
    value = input("Введите возраст друга: ")

    friend[key] = value
    friends.append(friend)

print(friends)

Main_name = ' '
Sum = 0

for friend in friends: # пробегаюсь по каждому словарю из списка
    for name in friend.keys(): # беру ключ из каждого списка
        Sum += int(friend[name])
        if len(Main_name) < len(name):
            Main_name = name

print("Средний возраст %.2f:" %(Sum / len(friends)))
print("Самое длинное имя:", Main_name)



print("\nЗадача 6: Описание задачи смотреть в коде программы\n")

'''
    Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
    Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов.
    В этой задаче нужно использовать строчный метод split().
'''

N = int(input("Введите количество слов: "))

Eng_dictionary = []

for index in range(N):
    
    word = dict()

    key = input("Введите английское слово: ")
    value = input("Введите перевод этого слова: ")

    word[key] = value.split(" |,")
    Eng_dictionary.append(word)

print(Eng_dictionary)