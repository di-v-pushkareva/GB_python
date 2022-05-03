spisok = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг - {spisok}")
reiting = int(input("Введите число (111 - выход) "))
while reiting != 111:
    for el in range(len(spisok)):
        if spisok[el] == reiting:
            spisok.insert(el + 1, reiting)
            break
        elif spisok[0] < reiting:
            spisok.insert(0, reiting)
        elif spisok[-1] > reiting:
            spisok.append(reiting)
        elif spisok[el] > reiting and spisok[el + 1] < reiting:
            spisok.insert(el + 1, reiting)
    print(f"текущий рейтинг - {spisok}")
    reiting = int(input("Введите значение "))