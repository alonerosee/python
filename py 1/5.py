import math
x = 0
a = int(input("Введите значение первого коэффициента:"))
b = int(input("Введите значение второго коэффициента:"))
c = int(input("Введите значение третьего коэффициента:"))
y = ((a*x)**2)+b*x+c == 0
d = (b**2)-4*a*c
if d > 0:
    print("Квадратное уравнение имеет 2 корня")
elif d < 0:
    print("Квадратное уравнение имеет 1 корень")
else:
    print("Корней нет")
