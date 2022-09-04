dict={
                1:'x= от 0 до ∞ & y= от 0 до ∞',
                2:'x= от 0 до ∞ & y= от 0 до -∞',
                3:'x= от 0 до -∞ & y= 0 от -∞',
                4:'x= от 0 до -∞ & y= от 0 до ∞'
                 }
def length_A_B(a:[],b:[])->float:
    """получение длинны отрезка"""
    return ((b[0]-a[0])**2+(a[1]-b[1])**2)**(0.5)
def enter_num(enterN:int)->[]:
    """получение переменных x,y,z"""
    pred=['x','y','z']
    result=[]
    for i in range(enterN):
        result.append(int(input(f'введите значение {pred[i]}')))
    return result
def check_pred(list_coordinates:[])->bool:
    """проверка предиката"""
    left = ~(list_coordinates[0] | list_coordinates[1] | list_coordinates[2])
    right = ~ list_coordinates[0] & ~ list_coordinates[1] & ~ list_coordinates[2]
    result=left==right
    return result

def input_coord(c_point:int)->[]:
    """ввод координат"""
    xy=['X','Y']
    result=[]
    for i in range(c_point):
        try:
            number=int(input(f'введите координату по оси {xy[i]}:'))
            result.append(number)
        except ValueError:
            print('введите целые числа)')
    return result

"""программa, которая принимает на вход цифру, обозначающую день недели,\ 
и проверяет, является ли этот день выходным."""
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

day_w=1
text='определение, являеться ли день недели выходным.\
\nвведите номер дня недели, для перехода к следующей задаче, введите 0 :\n'    
while day_w!=0:
   try:
      day_w=int(input(text))
      if 0<day_w<6:
        print('нет')
      elif day_w==6 or day_w==7:
        print('да')
      elif day_w==0:
        continue
      else: print('нет такого дня недели')
   except ValueError:
       print('введено не число, попробуйте снова')
else: print('конец вычисления дней недели, следующая задача:\
\n проверка истинности утверждения для предиката:\n')
user_exit=1    
"""программа для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \
для всех значений предикат."""
while user_exit !=0:
    
    try:
        user_exit=int(input('продолжить вычисления(1), завершить(0)\n'))
        if user_exit==0:
            continue
        else:
            coordinates = enter_num(3)
            #if check_pred(coordinates):
             #   print("истинно")
            #else: print('ложно')
            print(check_pred(coordinates))
    except ValueError:
        print('не верные данные, попробуте снова')
else: print('следующая задача. принимает на вход координаты точек Х,У. \
выдает номер четверти плоскости:\n')

#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3
usrer_exit=1
while usrer_exit !=0:
    try:
        x=float(input('введите значение х:\n'))
        y=float(input('введите значение y:\n'))
        if x==0 or y==0:
             print('не соответствует условию')
        elif x>0:
            if y>0:
                print('-> 1')
            elif y<0:
                print('-> 2')
        elif x<0:
            if y<0:
                print('-> 3')
            elif y>0:
                print('-> 4')
        usrer_exit=int(input('выйти введите 0, ввести еще координаты введите 1:\n'))

    except ValueError:
        print('не верные данные, попробуте снова')
    else: print('следующая задача. по заданному номеру четверти, показать диапазон возможных\
координат точек в этой четверти:')
user_exit=1
while user_exit:
    try:
        user_exit=int(input('для выхода (0), продолжить (1)'))
        if not user_exit:
            continue
        else:
            num=int(input('введите номер четверти'))
            
            print(dict.get(num,'нет такой четверти'))
    except ValueError:
        print('ошибка ввода')
#Напишите программу, которая по заданному номеру четверти, показывает 
#диапазон возможных координат точек в этой четверти (x и y).
print('программа принимает на вход координаты двух точек и находит расстояние между ними:\n')
#Напишите программу, которая принимает на вход координаты двух 
#точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
user_exit=1

while user_exit:
    user_exit=int(input('для продолжения (1), выход(0)\n'))
    if not user_exit:
        break
    else:
        print('введите координату первой точки')
        Point1=input_coord(2)
        print('введите координату второй точки')
        Point2=input_coord(2)
        print(f"длинна отрезка = {format(length_A_B(Point1,Point2),'.2f')}")
       
