# 3) переделать первое задание под меню с помощью цикла
# Дан лист:
# my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
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
#         for num in my_list:
#             if my_list.count(num) > 1:
#                 my_list.remove(num)
#         for num in my_list:
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

