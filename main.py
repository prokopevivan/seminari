# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# n = int(input("Введите колличество монеток на столе:"))
# reshka = 0
# orel = 0
# for i in range(n):
#     storona =int(input(f"Введите какой стороной лежит {i+1} "
#                        f"монетка \n (1 - решка,0-орел):"))
#     if storona > 0:
#         reshka = reshka + 1
# else:
#         orel = orel+1
# if reshka<orel:
#     print(f"Нужно перевернуть {orel} монеты.")



sum_n_m = int(input('Первая подсказка: Сумма двух чисел (N и M от 0 до 1000) ->  '))
mult_n_m = int(input('2 подсказка: Произведение 2 чисел''(N и M от 0 до 1000) ->  '))
for i in range(0, 1001):
            for j in range(0, 1001):
                if i+j == sum_n_m and i*j == mult_n_m: print (f'Загаданые числа {i} и {j}')
else: print('таких чисел нет')


# number = int(input('Введите до какого числа будем выводить степени 2:  '))
# i = 0
# answer = []
# while 2 ** i < number:
#     temp = 2 ** i
#     answer.append(temp)
#     i += 1
# print(f'{number} -> {answer}')