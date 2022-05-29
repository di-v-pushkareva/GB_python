my_list = [3, 5, 5, 1, 9, 8, 11, 15, 9, 5]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)