# 3) переделать первое задание под меню с помощью цикла
# Дан лист:
# my_list = [1, 2, 2, 3, 4, 2, 2, 4, 2, 4, 4, 4, 2]
#
# while True:
#     print('1.найти min число в листе')
#     print('2.удалить все одинаковые значения')
#     print('3.заменить каждое четвертое значение на "Х"')
#     print('4.вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа')
#     print('5.Выход')
#     choice = input('Вибиріть число')
#
#     if choice == '1':
#         my_list.sort()
#         print('min_num', my_list[0])
#
#     elif choice == '2':
#         for num in my_list[::-1]:
#             if my_list.count(num) > 1:
#                 my_list.remove(num)
#         print(my_list)
#
#     elif choice == '3':
#         a = my_list.copy()
#         for i in range(3, len(a), 4):
#             a[i] = 'X'
#         print(a)
#
#     elif choice == '4':
#         num = (sum(my_list) / len(my_list))
#         my_list.append(num)
#         my_list.sort()
#         index = my_list.index(num)
#         small = my_list[index - 1]
#         big = my_list[index + 1]
#         right = big - num
#         left = num - small
#
#         if right > left:
#             print(small)
#         else:
#             print(big)
#
#     elif choice == '5':
#         break
#
#     else:
#         print('Такого числа немає')
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# side = 10
# i = side
# while i >= 1:
#     if i == side or i == 1:
#         j = side
#         while j > 0:
#             print('*', end='')
#             j -= 1
#         print()
#     else:
#         j = side - 2
#         print('*', end='')
#         while j > 0:
#             print(' ', end='')
#             j -= 1
#         print('*')
#     i -= 1
# 4) вывести табличку умножения с помощью цикла while
# i = 1
# size = 10
# while i <= size:
#     j = 1
#     while j <= size:
#         res = i * j
#         if res // 10:
#             print(res, end='  ')
#         else:
#             print(res, end='   ')
#         j += 1
#     print()
#     i += 1
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
# costs = [{'date': '23.02', 'name': 'milk', 'price': 20},
#          {'date': '20.02', 'name': 'bread', 'price': 25}]
#
# while True:
#     print('1) Создать запись')
#     print('2) Список все записей')
#     print('3) Общая сумма всех покупок')
#     print('4) Самая дорогая покупка')
#     print('5) Поиск по названию покупки')
#     print('6) Поиск по дате')
#     print('7) Выход')
#
#     choice = input('Зробіть свій вибір')
#
#     if choice == '1':
#         date = input('Введіть дату (XX:XX)')
#         name = input('Введіть назву')
#         price = int(input('Ціна :'))
#
#         costs.append({'date': date, 'name': name, price: price})
#
#     elif choice == '2':
#         print(costs)
#
#     elif choice == '3':
#         spending = 0
#         for cost in costs:
#             spending += cost.get('price')
#         print(spending)
#
#     elif choice == '4':
#         maxPrice = {'date': '12.05', 'name': 'test', 'price': 0}
#         for cost in costs:
#             if cost['price'] > maxPrice['price']:
#                 maxPrice.update(cost)
#         print(maxPrice)
#
#     elif choice == '5':
#         findName = input('Введіть назву товару')
#
#         for cost in costs:
#             if cost['name'] == findName:
#                 print(cost)
#
#     elif choice == '6':
#         findDate = input('Введіть дату (ХХ:ХХ)')
#
#         for cost in costs:
#             if cost['date'] == findDate:
#                 print(cost)
#
#     elif choice == '7':
#         break
#
#     else:
#         print('Введіть число із списку')
