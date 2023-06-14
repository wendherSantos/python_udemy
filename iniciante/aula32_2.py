"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite o seu primeiro nome: ')
nome_curto = primeiro_nome <= primeiro_nome[:4]
nome_normal = primeiro_nome >= primeiro_nome[:5] and primeiro_nome <= primeiro_nome[:6]

if nome_curto:
    print('Seu nome é curto')
elif nome_normal:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1 and tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')
elif tamanho_nome > 6:
    print('Seu nome é grande')
else:
    print('Digite mais que uma letra')