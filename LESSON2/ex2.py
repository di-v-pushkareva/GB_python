el_kolvo = int(input("Введите количество элементов  "))
spisok = []
i = 0
el = 0
while i < el_kolvo:
    spisok.append(input("Введите  значение списка "))
    i += 1

for elem in range(int(len(spisok)/2)):
        spisok[el], spisok[el + 1] = spisok [el + 1], spisok[el]
        el += 2
print(spisok)