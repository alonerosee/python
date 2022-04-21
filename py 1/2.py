import math
x = int(input("Введите число для переменной x:"))
y = int(input("Введите число для переменной y:"))

h = math.sqrt(math.cos(2*y)+math.sin(4*y)+math.sqrt(math.exp(x)+math.exp(-x)))/((math.exp(-x)+math.exp(x))**3)*(math.sin(4*y)+math.cos(2*y)-2)**2
print("h = {0:.2f}".format(h))
