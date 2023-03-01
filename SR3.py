#Задание 3.1
import math
x1 = float(input('Введите от:'))
x2 = float(input('и до какого значения рассматриваем функцию:'))
h = float(input('Введите шаг смещения по оси x:'))
l = []
while round(x1, 1) <= x2:
    l.append(str(round((1 + x1 * x1) / 2 * math.atan(x1) - x1 / 2, 5)) + ',' + ' ' + 'При х = ' + str(round(x1, 2)))
    x1 += h
print(l)

def funtext(x1,x2,h)   
    l = []
    while round(x1, 1) <= x2:
        l.append(str(round((1 + x1 * x1) / 2 * math.atan(x1) - x1 / 2, 5)) + ',' + ' ' + 'При х = ' + str(round(x1, 2)))
        x1 += h
    print(l)
funtext(x1 = float(input('Введите от:')),x2 = float(input('и до какого значения рассматриваем функцию:')), h = float(input('Введите шаг смещения по оси x:')))




#Задание 3.2
import string
     file_contents = myfile.read().splitlines()
     print(file_contents.pop(k))
textsplit(k=int(input('Введите номер строки из текста>>>')))
textsplit(k=int(input('Введите номер строки из текста>>>')))
