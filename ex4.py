n = int(input("Введите число "))
max = 0
while n > 10:
    d = n % 10
    n //= 10
    if d > max:
        max = d
print(max)