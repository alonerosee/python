# Тройная проверка
number = 14
if number > 10 or number != 12 or number <= 15 or number == 18:
   print("number - True")

# Самостоятельный цикл do...while
num = 10
while True: # Сперва выполняем цикл
	num -= 1
	if num == 0: # Далее прописываем проверку
		break

# Работа с циклами
i = 34
while i <= 67:
	if i % 2 != 1:
		print (i)
	i += 1

# Вывод чисел
x = 1
while x <= 100:
   if x == 50 or x == 99:
      continue
   print(x)
   x += 1   
