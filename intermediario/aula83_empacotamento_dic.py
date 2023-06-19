# Empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.8,
}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NAO NOMEAODS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoa_completa)

configs = {
    'args 1': 1,
    'args 2': 2,
    'args 3': 3,
    'args 4': 4,
}

# for chave, valor in configs.items():
#     print(chave, valor)

mostro_argumentos_nomeados(**configs)