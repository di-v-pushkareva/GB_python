def div(*args):

    try:
        arg1 = int(input("Введите делимое "))
        arg2 = int(input("Введите делитель "))
        res = arg1 / arg2

    except ZeroDivisionError:
        return "Ошибка. Дельнить на ноль нельзя!"

    return res

print(f'Результат деления: {div()}')
