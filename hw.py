a=int(input('input a number1: '))
b=int(input('input a number2: '))
c=int(input('input a number3: '))

print('\na=',a,'\nb=',b,'\nc=',c)

if a*b==c:
    print('\nпроизведение чисел a и b равно числу c')
else:
    print('\nпроизведение чисел a и b не равно c')

if a*c+b==0:
    print('c является решением линейного уравнения a*x+b=0')
else:
    print('c не является решением линейного уравнения a*x+b=0')
