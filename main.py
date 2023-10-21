RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[30m'
END = '\u001b[0m'

# for i in range(6):
#     if i < 2:
#         print(f'{RED}{"  " * 14}{END}')
#     elif i > 1 and i < 4:
#         print(f'{WHITE}{"  " * 14}{END}')
#     else:
#         print(f'{BLUE}{"  " * 14}{END}')


# plot_list = [[0 for i in range(10)] for i in range(10)]
# result = [0 for i in range(10)]

# for i in range(10):
#     result[i] = 2 * i

# step = round(abs(result[0] - result[9]) / 9, 2)

# for i in range(10):
#     for j in range(10):
#         if j == 0:
#             plot_list[i][j] = step * (8-i) + step

# for i in range(9):
#     for j in range(10):
#         if abs(plot_list[i][0] - result[9 - j]) < step:
#             for k in range(9):
#                 if 8 - k == j:
#                     plot_list[i][k+1] = 1

# for i in range(9):
#     line = ''
#     for j in range(10):
#         if j == 0:
#             line += '\t' + str(int(plot_list[i][j])) + '\t'
#         if plot_list[i][j] == 0:
#             line += '--'
#         if plot_list[i][j] == 1:
#             line += '!!'
#     print(line)
# print('\t0\t1 2 3 4 5 6 7 8 9')

# for i in range(10):
#     print(plot_list[i])
#     pass

# file = open('sequence.txt', 'r')
# list = []
# for number in file:
#     list.append(float(number))
# file.close()
# sum_nechet = 0
# sum_chet = 0
# for i in range(len(list)):
#     if i % 2 == 0:
#         sum_nechet += list[i]
#     else:
#         sum_chet += list[i]
# print(round(sum_chet,2), round(sum_nechet, 2))

# nechet = []
# chet = []
# for i in range(len(list)):
#     if i % 2 == 0:
#         nechet.append(float(list[i]))
#     else:
#         chet.append(float(list[i]))
# print(round(sum(nechet),2), round(sum(chet),2))

# size = 20
# for i in range(size):
#     for j in range(size):
#         if i == j or i + j == size - 1:
#             print(f'{WHITE}{"  " * 1}{END}', end =" ")
#         else:
#             print(" ", end="")
#     print()


# WHITE = '\u001b[47m'
# BLACK = '\u001b[97m'
# RESET = '\u001b[0m'  # Для сброса цветов после окончания крестика

# def draw_two_black_crosses_45_degrees(size):
#     for i in range(size):  # Итерируемся по строкам (горизонталь)
#         # Рисуем первый крестик (левый) с черными символами на белом фоне
#         for j in range(size):  # Итерируемся по столбцам (вертикаль)
#             if i == j or i + j == size - 1:  # Условие для рисования крестика
#                 print(f"{WHITE}  {RESET}", end='')  # Выводим два пробела с белым фоном
#             else:
#                 print(f"{BLACK}  {RESET}", end='')  # Выводим два пробела с черными символами на белом фоне
#         # Рисуем второй крестик (правый) с черными символами на белом фоне
#         for j in range(1, size):  # Итерируемся по столбцам, начиная с индекса 1
#             if i == j or i + j == size - 1:  # Условие для рисования крестика
#                 print(f"{WHITE}  {RESET}", end='')  # Выводим два пробела с белым фоном
#             else:
#                 print(f"{BLACK}  {RESET}", end='')  # Выводим два пробела с черными символами на белом фоне
#         print()  # Переходим на следующую строку после завершения рисования обоих крестиков

# # Пример использования:
# draw_two_black_crosses_45_degrees(11)  # Вызываем функцию с размером 11 для вывода узора




# def draw_dutch_flag():
#     # Определение цветов
#     RED = '\u001b[41m'
#     WHITE = '\u001b[47m'
#     BLUE = '\u001b[44m'
#     RESET = '\u001b[0m'

#     # Размер флага
#     width = 18  # Ширина флага
#     height = 6  # Высота флага

#     # Рисуем флаг Нидерландов
#     for i in range(height):
#         if i < height // 3:
#             color = RED
#         elif i < 2 * height // 3:
#             color = WHITE
#         else:
#             color = BLUE

#         for j in range(width):
#             print(f"{color}  {RESET}", end='')

#         print()

# # Пример использования:
# draw_dutch_flag()

# import matplotlib.pyplot as plt
# import numpy as np

# # Создаем массив значений x от -10 до 10 с шагом 0.1
# x = np.arange(-10, 10, 0.1)

# # Вычисляем соответствующие значения y = 2x
# y = 2 * x

# # Строим график
# plt.plot(x, y, label='y = 2x')

# # Добавляем заголовок и метки осей
# plt.title('График функции y = 2x')
# plt.xlabel('x')
# plt.ylabel('y')

# # Включаем сетку
# plt.grid(True)

# # Добавляем легенду
# plt.legend()

# # Отображаем график
# plt.show()