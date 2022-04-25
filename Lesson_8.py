# СЛОВАРИ В PYTHON

''' Словарь — неупорядоченная структура данных, которая позволяет хранить пары «ключ — значение» '''

# Создание словаря c помощью литерала

student = {'name': 'Ivan', 'age': 12}
credentials = {'email': 'hacker1337@gmail.ru', 'password': '123456'}

# Создание словаря c помощью функции dict()
student = dict(name = 'Ivan', age = 12)
credentials = dict(email = 'hacker1337@mail.ru', password = '123456')


# Получаем значение с ключом 'name'
print("\nИмя студента через ключ 'name':", student['name']) # -> Ivan
print("Возраст студента через ключ 'age':", student['age']) # -> 12


print("\n===================================================\n")


#Обновление существующих значений происходит абсолютно также

student = dict(name = 'Yaroslav', age = 18)
print("Имя студента через ключ 'name' до изменения:", student['name']) # -> Yaroslav
print("Возраст студента через ключ 'age' до изменения:", student['age']) # -> 18

student['name'] = 'Vasiliy'
student['age'] = '22'
print("\nИмя студента через ключ 'name' после изменения:", student['name']) # -> Vasiliy
print("Возраст студента через ключ 'age' после изменения:", student['age']) # -> 22


print("\n===================================================\n")

phone = dict(Model = 'Samsung', price = '9990')
print("Словарь до удаления:", phone)

del phone['price']
print("Словарь после удаления:", phone)


print("\n===================================================\n")


'''
    Метод get() возвращает значение по указанному ключу.
    Если указанного ключа не существует, метод вернёт None.
    Также можно указать значение по умолчанию, которое будет 
    возвращено вместо None, если ключа в словаре не окажется.
'''

car = dict(color = 'red', price = '15999')

# словарь.get('ключ', 'если нет ключа')
print("Цвет машины:", car.get('color'))
print("Модель машины:", car.get('model'))
print("Модель машины:", car.get('model', 'No model'))


print("\n===================================================\n")


''' Метод pop() удаляет ключ и возвращает соответствующее ему значение '''

sneakers = dict(brand = 'Adidas', price = '9990 RUB', model = 'Nite Jogger')
print("Словарь до метода .pop():", sneakers)

model = sneakers.pop('model')
print("\nСловарь после метода .pop():", sneakers)
print("model =", model)


print("\n===================================================\n")


''' Метод keys() возвращает специальную коллекцию ключей в словаре '''

sneakers = dict(brand = 'Adidas', price = '9990 RUB', model = 'Nite Jogger')

print("Коллекция ключей в словаре:", sneakers.keys())
print("dict_keys - это неизменяемая коллекция элементов\n")

# Если мы хотим получить просто список ключей без лишних слов, то:

print("Список ключей в словаре:", list(sneakers.keys()))


print("\n===================================================\n")


''' Метод values() возвращает специальную коллекцию значений в словаре '''

sneakers = dict(brand = 'Adidas', price = '9990 RUB', model = 'Nite Jogger')

print("Коллекция значений в словаре:", sneakers.values())
print("dict_keys - это неизменяемая коллекция элементов\n")

# Если мы хотим получить просто список ключей без лишних слов, то:

print("Список значений в словаре:", list(sneakers.values()))


print("\n===================================================\n")


''' Метод items() возвращает пары «ключ — значение» в формате кортежей '''

sneakers = dict(brand = 'Adidas', price = '9990 RUB', model = 'Nite Jogger')

print("Коллекция пар в словаре:", sneakers.items())
print("dict_keys - это неизменяемая коллекция элементов\n")

# Если мы хотим получить просто список ключей без лишних слов, то:

print("Список пар в словаре:", list(sneakers.items()))


print("\n===================================================\n")


''' Способы вывода ключей, значений '''

phone = dict(brand = 'Samsung', price = '45990 RUB', model = 'Samsung S22 Ultra')

# вывод ключей при помощи цикла for

for key in phone.keys(): # .keys() можно не писать
    print(key)
print()

# вывод значений при помощи цикла for

for value in phone.values():
    print(value)
print()

# вывод ключей и значений при помощи цикла for

for key, value in phone.items():
    print(key, value, sep = ' - ')


print("\n===================================================\n")


''' Метод setdefault() возвращает значение ключа, но если его нет, создает ключ с указанным значением (по умолчанию None) '''

student = dict(name = 'Alexsandr', age = 24)
print(student)

student.setdefault('lastname', 'Kamenev')
print(student)






