"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibiliade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
num_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    num_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU! PARABÉNS!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {num_tentativas}')
        letras_acertadas = ''
        num_tentativas = 0