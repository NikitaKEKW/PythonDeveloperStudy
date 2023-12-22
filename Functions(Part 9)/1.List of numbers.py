def reverse_numbers(n):
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n = n // 10
    return digits


n = 576038100
result = reverse_numbers(n)
print("Исходное число:", n)
print("Результат:", result)
