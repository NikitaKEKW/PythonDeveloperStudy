while True:
    try:
        amount = float(input("Введите число: "))
        if amount > 0:
            amount = round(amount, 2)
            formatted_amount = "{:,.2f}".format(amount)
            print("Сумма:", formatted_amount)
            break
        else:
            print("Число должно быть больше 0. Попробуйте еще раз.")
    except ValueError:
        print("Ошибка: Некорректный ввод.")
