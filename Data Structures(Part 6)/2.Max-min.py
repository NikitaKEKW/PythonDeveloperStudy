elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if len(elements) == 0:
    result = 0
    print("В списке нет элементов:", result)
else:
    result = round(max(elements) - min(elements), 3)
    print("Результат:", result)
