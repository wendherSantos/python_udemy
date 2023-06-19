# Exemplo de uso dos sets

letras = set()

while True:
    letra = input('Digite a letra secreta: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)

