# isinstance - para saber se objeto é de determinado tipo
# isinstance - to check if an object is of a certain type
# é instância de

lst = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Wendher'}
]

for item in lst:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUMBER')
        print(item, item * 2)
    
    else:
        print('OTHER')
        print(item)