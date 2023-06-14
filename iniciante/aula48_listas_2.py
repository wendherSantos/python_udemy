"""
Listas em Python
Tipo list - mutável
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: append, insert, pop, del, clear, extend, +
Create Read  Update   Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""

lista = [10, 20, 30, 40]
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(f'{lista} \nRemovido {ultimo_valor}')