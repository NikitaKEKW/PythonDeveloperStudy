while True:
    decimal_number = int(input("Введите число от 1 до 3999 - "))
    if decimal_number < 1 or decimal_number > 3999:
        print("Число должно входить в промежуток от 1 до 3999")
    else:
        dec_to_latin = {
            1000: 'M', 900: 'CM',
            500: 'D', 400: 'CD',
            100: 'C', 90: 'XC',
            50: 'L', 40: 'XL',
            10: 'X', 9: 'IX',
            5: 'V', 4: 'IV', 1: 'I', }
        latin_number = ''
        break
for value, symbol in dec_to_latin.items():
    while decimal_number >= value:
        decimal_number -= value
        latin_number += symbol
print("Результат -", latin_number)
