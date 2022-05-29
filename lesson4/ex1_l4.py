from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, bonus = argv
    time_work = int(time_work)
    rate = int(rate)
    bonus = int(bonus)
    print((time_work * rate) + bonus)
else:
    time_work = int(input("Введите выработку в часах: "))
    rate = int(input("Введите ставку: "))
    bonus = int(input("Введите премию: "))
    print((time_work * rate) + bonus)