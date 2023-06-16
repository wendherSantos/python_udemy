# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

person = {
    'name': 'Wendher Gerson dos Santos',
    'surname': 'Miranda',
    'age': 20,
    'height': 1.70,
    'adresses': [
        {'rua': 'tal tal', 'number': 123},
        {'rua': 'other tal', 'number': 323},
    ],
}

# print(person, type(person))
print(person['name'])
print(person['surname'])

print()

for i in person:
    print(i, person[i])
