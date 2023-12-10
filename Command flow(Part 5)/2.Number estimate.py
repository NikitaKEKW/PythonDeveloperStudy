from random import randint

number = randint(0, 30)
result = ("Плохо - {number}".format(number=number) if (number % 2 != 0) else
          "Неплохо - {number}".format(number=number)
          if (number >= 2) and (number <= 5) and (number % 2 == 0) else
          "Так себе - {number}".format(number=number)
          if (number >= 6) and (number <= 20) and (number % 2 == 0) else
          "Отлично - {number}".format(number=number)
          if (number > 20) and (number % 2 == 0) else "")
print(result)
