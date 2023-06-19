# Dictionary Comprehension and Set  Comprehension

products = {
    'name': 'Caneta Azul',
    'price': 2.5,
    'category': 'Escritório',
}

dic = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in products.items()
    if key != 'category'
}

lst = [
    ('a', 'valor a'),
    ('b', 'valor n'),
    ('c', 'valor c'),
]

dc = {
    key: value
    for key, value in lst
}

st1 = {2 ** i for i in range(10)}

print(st1)