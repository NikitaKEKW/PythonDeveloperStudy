from random import randint

num1 = randint(0, 100)
num2 = randint(0, 100)
num3 = randint(0, 100)
print(" Первое число: {num1} \n Второе число: {num2} \n Третье число: {num3} \n Результат:   "
      .format(num1=num1, num2=num2, num3=num3),
      round(num1 + num2 + num3 / 3))
