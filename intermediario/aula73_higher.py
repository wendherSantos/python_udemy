"""
Higher Ordem Functions
Funcões de Primeira Classe
"""
"""
Termos técnicos: Higher Order Functions e First-Class Functions

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.
    Higher Order Functions - Funções que podem receber e/ou retornar outras funções
    First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.
Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.

"""

def salutation(msg, name):
    return f'{msg}, {name}'

def execute(funcao, *args):
    return funcao(*args)


print(
    execute(salutation, 'Bom dia', 'Wendher!')
      )

print(
    execute(salutation, 'Bom dia', 'Maria!')
      )
