from random import randint

number = randint(0, 1000)
result = ("Fuzz Buzz - {number}".format(number=number) if number % 3 == 0 and number % 5 == 0 else
          "Fizz - {number}".format(number=number) if number % 3 == 0 else
          "Buzz - {number}".format(number=number) if number % 5 == 0 else
          "Нет такого числа")
print(result)
