stroka = input("введите строку ")
slovo = []
num = 1
for el in range(stroka.count(' ') + 1):
    slovo = stroka.split()
    if len(str(slovo)) <= 10:
        print(f" {num} {slovo [el]}")
        num += 1
    else:
        print(f" {num} {slovo [el] [0:10]}")
        num += 1