# ФУНКЦИИ В PYTHON

"""
    Функция - это именованный блок кода, к которому можно обратиться из любого места программы.
    У функции есть имя и список входных параметров, а также возвращаемое значение.
    
    Функция позволяет использовать в программе один и тот же фрагмент кода несколько раз.
"""
# Oбъявление функции в Python выглядит так:

def function_name(argument1, argument2):
    print("Код функции тут!")

# def - DEclare Function - "объявить функцию"
# function_name - имя функции
# (argument1, argument2, ...) - список аргументов, поступающих на вход функции при ее вызове
# тело функции - это весь код, который идет после двоеточия

print() # для отступа в консоли


def Hello(name):
    print("Hello, " + name + "!")

# Вызов функции

Hello("Max")
Hello("Ivan")
Hello("Kate")


def sum(a, b):
    return a + b # return возвращает значение a + b

print("\n5 + 10 =", sum(5, 10))
print("423 + (-123) =", sum(423, -123))
print("521 + 4123 =", sum(521, 4123), end = '\n\n')


'''
    Для параметров функции можно указывать значения по умолчанию.
    Это дает возможность вызывать функцию с меньшим числом параметров.
'''

# Аргумент name по умолчанию равен 'world'

def hello(name = 'world'):
    print("Hello, " + name + "!")

hello() # если ничего не будет в аргументе, то тогда name примит значение по умолчанию name = world
hello('Ivan')


print("\n==========================================\n")


# Примеры функций

# Квадрат числа 
def square(number):
    return number * number 

print("Квадрат числа 17:", square(17), end = '\n\n')


# Периметр прямоугольника(квадрата)
def perimetr(a, b):
    return 2 * (a + b)

print("Периметр со сторонами 14 и 19:", perimetr(14, 19), end = '\n\n')


# Чётиное число или нет
def isEven(x):
    return x % 2 == 0

print("Чётное число 10?", isEven(10))
print("Чётное число 11?", isEven(11), end = '\n\n')


# Вернуть сумму всех элементов списка
def Amount_List(lst):
    amount = 0
    for x in lst:
        amount += x
    return amount

mylist = [1, 2, 4, 8, 16]

print('Сумма списка', mylist, '=', Amount_List(mylist))


# Фибоначчи: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
def Fib(N):

    F1 = F2 = 1

    if N == 1 or N == 2: 
        return F1

    i = 0
    FN = 0

    for i in range(0, N - 2):
        FN = F1 + F2
        F1 = F2
        F2 = FN
        
    return FN

print("Fib(1) = ", Fib(1))
print("Fib(2) = ", Fib(2))
print("Fib(3) = ", Fib(3))
print("Fib(4) = ", Fib(4))
print("Fib(5) = ", Fib(5))
print("Fib(10) = ", Fib(10))
print("Fib(20) = ", Fib(20), end = '\n\n')


# Факториал

def Fact(N):

    F = 1

    if N == 0 or N == 1:
        return F

    elif N > 1:
        while N > 1:
            F *= N
            N -= 1
    
    else:
        print("ERROR\n")

    return F

print("Fact(5) = ", Fact(5))
print("Fact(6) = ", Fact(6))
print("Fact(10) = ", Fact(10))
print("Fact(13) = ", Fact(13), end = '\n\n')







