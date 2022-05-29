from itertools import cycle

my_list = ['беконечный цикл', 111]
for el in cycle(my_list):
    print(el)