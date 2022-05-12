

def my_func(name, lastname, year, city, email, telephone):
    return ' '.join([name, lastname, year, city, email, telephone])
print(my_func(lastname = 'Иванов', name = 'Иван', year = '1996', city = 'Москва', email = 'info@mail.ru', telephone = '88005553535'))