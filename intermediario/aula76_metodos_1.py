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
person = {
    'name': 'Marvel DC',
    'surname': 'Wendher 1',
    # 'idade': 900,
}

person.setdefault('idade', '???')
print(person['idade'])
# print(len(person))
# print(list(person.keys()))
# print(list(person.values()))
# print(list(person.items()))



# for chave in person:
#     print(chave)

# for chave, valor in person.items():
#     print(chave, valor)