num1 = input("Исходное число: ")
num1 = str(num1)
num2 = num1[::-1]
num2 = str(num2)
if (int(num2) > pow(2, 31) - 1) or (int(num2) < -pow(2, 31) - 1):
    print("Число выходит за границу")
else:
    print("Обратное число:", str(num2))
