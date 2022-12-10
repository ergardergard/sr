# # Задание 2.1
import math
i = int(float(input('введите первое ограничение'))*10)
e = int(float(input('введите второе ограничение'))*10)
h = int(float(input('введите шаг '))*10)
p=' '
print ('x:',10*p,'y:')
for i in range (i,e+1,h):

    x = i/10

    y = (8.364 - 2.326 * 2*x )/(math.sqrt(1.364 * x*2 + 1.247))
    print (x,10*p,y)
    
    
    
    
    # Задание 2.1
    import math
si =0
n  = int(input('введите начало'))
n1 = int(input('введите конец'))
for n in range (n,n1+1):
    si = si + math.sin(1/n)
s = (2/5 + si ) / 6 
print (s)




    # Задание 2.3
    n = int(input('введите n'))
i = 0
x = 0
p = ' '
fak = 0
st = int(input ('сумму какого столбца вам нужна  '))
for i in range (n,0,-1):
    int(x)
    x = x + 1
    y = n - i
    x1 =  str(x)
    if len(x1)== 1:
        print((p+x1+p)*i,('0' +p*2)*y )
    else :
        print((p+x1)*i,('0' +p*2)*y )
for st in range (0,n+2 - st):
    fak =  fak + st
print(fak)

