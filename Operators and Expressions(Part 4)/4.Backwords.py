from random import randint

number = randint(100, 1000)
number_str = str(number)
backwords_number = number_str[::-1]
print(" Исходное число равно {number}\n Обратное число равно {backwords_number} "
      .format(number=number, backwords_number=backwords_number))
