
# Задание 1
x = float(input('введите x'))
y = float(input('введите y'))
if ((-0.5 <= x <= 3.5) and (y==1 or y == 2.8)) or ((1 <= y <= 2.8 ) and (x==-0.5 or x==3.5)):
    print('на границе')
    if x == -0.5:
        x = x + 1
    elif x == 3.5 :
        x = x - 1
    if y == 2.8:
        y = y -1
    elif y== 1 :
        y = y + 1
    print('x=',x)
    print('y=',y)
elif (-0.5 <= x <= 3.5) and (1 <= y <= 2.8 ):
    print ('принадлеж')
    print('S= ',4*1.8)
    print('p= ',4*2+1.8*2)
else:
    print('не принадлеж')
    strok1 = input('введите строку')
    strok2 = input('введите строку')
    strok = max(len(strok1),len(strok2))
    if len(strok1) == strok:
        abc = strok1
    else:
        abc = strok2
    s = 4 * 1.8
    if s > strok:
        print('s>',abc)
    elif s < strok:
        print('s<',abc)
        
        
        
