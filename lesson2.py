# Strings
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# введена строка
# st = 'as 23 fdfdg544'
# result = ''
#
# for i in st:
#     if i.isdecimal():
#         result += i
# result = ', '.join(result)
# print(result)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34'
# result = ''
#
# for i in st:
#     if i.isdigit():
#         result += i
#     else:
#         result += " "
# result = ', '.join(result.split())
# print(result)


# #################################################################################
#


# list comprehension
#
# 1)есть строка:
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# greeting = 'Hello, world'
# upper_greeting = [i.upper() for i in greeting]
# print(upper_greeting)
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# Як в умові
# l = [i ** 2 for i in range(50) if i % 2 != 0]
# print(l)
# Як в прикладі
# l = [i ** 2 for i in range(50)]
# print(l)


# function
#
# - створити функцію яка виводить ліст
# l = [1, 32, 4, 5, 6, 76]
#
#
# def list_func(l):
#     for i in l:
#         print(f'[{l.index(i)}]-> {i}')
#
#
# list_func(l)
# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def num_min(num1, num2, num3):
#     res = min(num1, num2, num3)
#     print(res)
#     return res
#
#
# num_min(3, 7, 10)
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def num_max(num1, num2, num3):
#     res = max(num1, num2, num3)
#     print(res)
#     return res
#
#
# num_max(32, 9, 7)
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def num_func(*args):
#     res_min = min(args)
#     res_max = max(args)
#     print(res_max)
#     return res_min
#
#
# num_func(232, 434, 7, 8, 9, 0)
# - створити функцію яка повертає найбільше число з ліста
# l = [1, 23, 4, 5, 6, 7, 8, 8]
# def list_func(*args):
#     return max(args)
#
#
# print(list_func(*l))
# - створити функцію яка повертає найменьше число з ліста
# l = [1, 23, 4, 5, 6, 7, 8, 8]
#
#
# def list_func(*args):
#     return min(args)
#
#
# print(list_func(*l))
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# l = [1, 23, 4, 5, 6, 7, 8, 8]
#
#
# def sum_func(*args):
#     return sum(args)
#
#
# print(sum_func(*l))
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# l = [1, 23, 4, 5, 6, 7, 8, 8]
#
#
# def avg_func(*args):
#     return sum(args) // (len(args))
#
#
# print(avg_func(*l))
# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
#
# def decorator(func):
#     def wrapper():
#         res = func().replace('_', ' ')
#         return res
#     return wrapper()
#
#
# @decorator
# def hello():
#     return 'Hello_boss_!!!'
#
#
# print(hello)
