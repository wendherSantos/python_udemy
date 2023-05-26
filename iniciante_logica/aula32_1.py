"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num = input('Digite um número inteiro: ')

# if '.' in num:
#     print('Esse número não é inteiro')
# else:
#     num_inteiro = int(num)

#     if num_inteiro % 2 == 0:
#         print(f'O número {num_inteiro} é par!')
#     else:
#         print(f'O número {num_inteiro} é ímpar!')


num = input('Digite um número: ')

if num.isdigit():
    num_int = int(num)
    par_ou_impar = num_int % 2 == 0
    par_ou_impar_texto = 'impar'

    if par_ou_impar is True:
        par_ou_impar_texto = 'par'

    print(f'O número {num_int} é {par_ou_impar_texto}')
else:
    print('Você não digitou um número inteiro')