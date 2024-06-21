import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import random as rd

# Функция f(x) = 2^x
def mainfunc(n: float) -> float:
    return 2**n

# ---------------------------------------------------------------------------------
# Ввод границ
print('Введите левую границу:')
left_lim = int(input())
print('Введите правую границу:')
right_lim = int(input())

# ---------------------------------------------------------------------------------
# Данные для графика функции f(x)
x_axis = [value / 1000 for value in range(left_lim * 1000, right_lim * 1000)]
y_axis = [mainfunc(value) for value in x_axis]

fig = plt.figure()
graph = fig.add_subplot(111)
plt.axvline(x=0, color='black')
plt.axhline(y=0, color='black')
graph.scatter(0, 1, color='black')
plt.plot(x_axis, y_axis, color='magenta', linewidth='1.7')

# --------------------------------------------------------------------------------
# Способ оснащения: 1 - левый, 2 - правый, 3 - средний, 4 - случайный
print("Введите цифру 1 - 4, чтобы выбрать способ оснащения, в соответствии с:\n 1 - левый,\n 2 - правый,\n 3 - средний,\n 4 - случайный ")
fund_type = int(input())
print("Введите размерность разбиения n (частей):")
rect_smallish = int(input())

# Функции для вычисления интеграла разными способами

trapecia_mult = []
trapecia_result = 0

def left(left_lim, right_lim, rect_smallish, trapecia_mult, trapecia_result):
    counter = 0
    encount_axis = left_lim
    for i in range(rect_smallish):
        graph.add_patch(ptch.Rectangle((encount_axis, 0),
                                       ((right_lim - left_lim) / rect_smallish),
                                       mainfunc(encount_axis),
                                       edgecolor='cyan'
                                       ))
        counter += (right_lim - left_lim) * mainfunc(encount_axis) / rect_smallish
        encount_axis += (right_lim - left_lim) / rect_smallish
        trapecia_mult.append(mainfunc(encount_axis))
    for k in range(1, len(trapecia_mult)):
        trapecia_result += (trapecia_mult[k] + trapecia_mult[k - 1]) * (right_lim - left_lim) / (2 * rect_smallish)
    print(f"Значение интеграла: {counter},\nЗначение интеграла, вычисленным методом трапеций: {trapecia_result}")

def right(left_lim, right_lim, rect_smallish, trapecia_mult, trapecia_result):
    counter = 0
    encount_axis = left_lim
    for i in range(rect_smallish):
        encount_axis += (right_lim - left_lim) / rect_smallish
        k = encount_axis - (right_lim - left_lim) / rect_smallish
        graph.add_patch(ptch.Rectangle((k, 0),
                                       ((right_lim - left_lim) / rect_smallish),
                                       mainfunc(encount_axis),
                                       edgecolor='cyan'
                                       ))
        counter += (right_lim - left_lim) * mainfunc(encount_axis) / rect_smallish
        trapecia_mult.append(mainfunc(encount_axis))
    for k in range(1, len(trapecia_mult)):
        trapecia_result += (trapecia_mult[k] + trapecia_mult[k - 1]) * (right_lim - left_lim) / (2 * rect_smallish)
    print(f"Значение интеграла: {counter},\nЗначение интеграла, вычисленным методом трапеций: {trapecia_result}")

def center(left_lim, right_lim, rect_smallish, trapecia_mult, trapecia_result):
    counter = 0
    encount_axis = left_lim
    for i in range(rect_smallish):
        encount_axis += ((right_lim - left_lim) / rect_smallish) * 0.5
        k = encount_axis - (right_lim - left_lim) / (rect_smallish * 2)
        graph.add_patch(ptch.Rectangle((k, 0),


((right_lim - left_lim) / rect_smallish),
                                       mainfunc(encount_axis),
                                       edgecolor='cyan'
                                       ))
        counter += (right_lim - left_lim) * mainfunc(encount_axis) / rect_smallish
        encount_axis += ((right_lim - left_lim) / rect_smallish) * 0.5
        trapecia_mult.append(mainfunc(encount_axis))
    for k in range(1, len(trapecia_mult)):
        trapecia_result += (trapecia_mult[k] + trapecia_mult[k - 1]) * (right_lim - left_lim) / (2 * rect_smallish)
    print(f"Значение интеграла: {counter},\nЗначение интеграла, вычисленным методом трапеций: {trapecia_result}")

# Вызов соответствующей функции в зависимости от выбора пользователя
if fund_type == 1:
    left(left_lim, right_lim, rect_smallish, trapecia_mult, trapecia_result)
elif fund_type == 2:
    right(left_lim, right_lim, rect_smallish, trapecia_mult, trapecia_result)
elif fund_type == 3:
    center(left_lim, right_lim, rect_smallish, trapecia_mult, trapecia_result)
else:
    print("Неверный ввод. Программа завершена.")

plt.show()