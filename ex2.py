import datetime

sec = int(input("Введите количество секунд >>> "))
res = datetime.timedelta(seconds=sec)
print(res)