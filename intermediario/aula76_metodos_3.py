# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'name': 'Wendher',
    'surname': 'Legal',
}

# print(['name'])
# print(p1.get('name', 'Nao existe'))

# name = p1.pop('name')
# print(name)
# print(p1)

# last_key = p1.popitem()
# print(last_key)
# print(p1)

# p1.update({
#     'name': 'new value',
#     'age' : 30, 
# })

# p1.update(name='new value', idade=30)

tupla = ('name', 'new value'), ('age', 30)
# lista = ['name', 'new value'], ['age', 30]

p1.update(tupla)
print(p1)