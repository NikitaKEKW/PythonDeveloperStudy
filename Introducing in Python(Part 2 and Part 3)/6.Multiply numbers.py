def multiply_numbers(number):
    result = 1
    for digit in str(number):
        if digit != '0':
            result *= int(digit)
    return result


while True:
    try:
        number = int(input("Введите число: "))
        result = multiply_numbers(number)
        print("Результат:", result)
        break
    except ValueError:
        print("Ошибка: Некорректный ввод.")
