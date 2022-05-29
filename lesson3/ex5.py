def my_fun():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите значения. Для выхода введите Z').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'z' or number[el] == 'Z':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел: {sum_res}  Для выхода введите Z')
    print(f'Сумма числел {sum_res}')


my_fun()
