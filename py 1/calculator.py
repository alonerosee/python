firstNum = int(input("Введите первое число: "))
operand = input("Введите нужную операцию(+, -, *, /): ")
secondNum = int(input("Введите второе число: "))
if operand == "+" :
   print(firstNum + secondNum)
elif operand == "-":
   print(firstNum - secondNum)
elif operand == "*":
   print(firstNum * secondNum)
elif operand == "/" and secondNum == 0:
   print("Делить на ноль нельзя!!!")
elif operand == "/":
   print(firstNum / secondNum)
else:
   print("Произошла ошибка, возможно вы ввели неверный операнд")


