"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibiliade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

palavra_secreta = 'whadael'
tentativas = 0
adivinhadas = []

print('Bem-vindo ao jogo da adivinhação da palavra secreta!')
print(f'A palavra possui {len(palavra_secreta)} letras!')
print('Boa sorte!\n')

while True:
    letra = input('Digite uma letra: ')

    if len(letra) != 1:
        print('Erro: digite apenas uma letra!')
        continue

    if letra in adivinhadas:
        print("Erro: essa letra já foi digitada antes!")
        continue

    tentativas += 1
    adivinhadas.append(letra)

    if letra in palavra_secreta:
        print('Letra correta!')
        adivinhadas.append(letra)
    else:
        print('Letra incorreta!')
        adivinhadas.append('*')

    palavra_atual = ''
    for letra in palavra_secreta:
        if letra in adivinhadas:
            palavra_atual += letra
        else:
            palavra_atual += '*'

    print(f'Palavra atual: {palavra_atual}')

    if palavra_atual == palavra_secreta:
        print('Parabéns, você adivinhou a palavra secreta!')
        break

print(f'Números de tentativas {tentativas}')