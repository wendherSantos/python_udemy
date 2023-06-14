"""
Exercicio
Exiba os indices da lista
0 Maria
1 Helena
2 Wendher
"""

lista = ['Maria', 'Helena', 'Wendher']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))