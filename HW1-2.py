# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

a = int(input('Введите общее количество журавликов, которые сделали Петя, Катя, Серёжа:  '))
P = 0
K = 0
S = 0
if a % 6 == 0:
    S = a / 6
    K = 4 * S
    P = S
    print('Петя журавликов сделал: ')
    print(round(P))
    print('Катя журавликов сделала: ')
    print(round(K))
    print('Серёжа журавликов сделал: ')
    print(round(S))
else:
    print('Неправильно введено общее количество сделаных журавликов!!!')