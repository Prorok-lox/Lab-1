#Вариант-3
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[30m'
END = '\u001b[0m'


# def draw_dutch_flag():
#     for i in range(6):
#         if i < 2:
#             print(f'{RED}{"  " * 14}{END}')
#         elif i > 1 and i < 4:
#             print(f'{WHITE}{"  " * 14}{END}')
#         else:
#             print(f'{BLUE}{"  " * 14}{END}')
#     print()
# draw_dutch_flag()

# def draw_graphic_2x():
#     plot_list = [[0 for i in range(10)] for i in range(10)]
#     result = [0 for i in range(10)]

#     for i in range(10):
#         result[i] = 2 * i

#     step = round(abs(result[0] - result[9]) / 9, 2)

#     for i in range(10):
#         for j in range(10):
#             if j == 0:
#                 plot_list[i][j] = step * (8-i) + step

#     for i in range(9):
#         for j in range(10):
#             if abs(plot_list[i][0] - result[9 - j]) < step:
#                 for k in range(9):
#                     if 8 - k == j:
#                         plot_list[i][k+1] = 1

#     for i in range(9):
#         line = ''
#         for j in range(10):
#             if j == 0:
#                 line += '\t' + str(int(plot_list[i][j])) + '\t'
#             if plot_list[i][j] == 0:
#                 line += '--'
#             if plot_list[i][j] == 1:
#                 line += '!!'
#         print(line)
#     print('\t0\t1 2 3 4 5 6 7 8 9')
# draw_graphic_2x()


# def draw_two_crosses_45_degrees(size):
#     for i in range(size):
#         for j in range(size):  
#             if i == j or i + j == size - 1:  
#                 print(f"{WHITE}  {END}", end='')
#             else:
#                 print(f"{BLACK}  {END}", end='')
#         for j in range(1, size):  
#             if i == j or i + j == size - 1:  
#                 print(f"{WHITE}  {END}", end='')  
#             else:
#                 print(f"{BLACK}  {END}", end='')  
#         print()
# draw_two_crosses_45_degrees(11)


# def count_sum_2_ways():
#     file = open('sequence.txt', 'r')
#     list = []
#     for number in file:
#         list.append(float(number))
#     file.close()
#     sum_nechet = 0
#     sum_chet = 0
#     for i in range(len(list)):
#         if i % 2 == 0:
#             sum_nechet += list[i]
#         else:
#             sum_chet += list[i]
#     print(round(sum_chet,2), round(sum_nechet, 2))


#     nechet = []
#     chet = []
#     for i in range(len(list)):
#         if i % 2 == 0:
#             nechet.append(float(list[i]))
#         else:
#             chet.append(float(list[i]))
#     print(round(sum(chet),2), round(sum(nechet),2))
# count_sum_2_ways()