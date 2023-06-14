"""
Listas em Python
Tipo list - mutável
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis: 
    append - add um item ao final da lista
    insert - add um item no índice escolhido
    pop - remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read  Update   Delete
Criar, ler, alterar, apagar = lista [i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Wendher Gerson')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 'Wendher')
print(lista[4])