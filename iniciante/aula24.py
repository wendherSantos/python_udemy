# operadores in (está entre) e not in (nao está entre)
# strings sao iteraveis
# 0 1 2 3 4 5 6
# W e n d h e r
#-7-6-5-4-3-2-1

# nome = 'Wendher'

# print(nome[2])
# print(nome[-5])

# print(10 * '-')

# print('r' in nome)
# print('Wen' in nome)

# print(10 * '-')

# print('Wen' not in nome)
# print('r' not in nome)

# print(10 * '-')

nome = input('Digite o seu nome: ')

if ' ' in nome:
    print (f'seu nome {nome} contém espaços')
else:
    print (f'seu nome {nome} não contém espaços')