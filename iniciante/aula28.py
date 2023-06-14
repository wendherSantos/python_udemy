"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário digitar sua idade
Se nome e idade forem digitados:
    Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contém (ou não) espaços
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba: "Desculpe, voce deixou campos vazios."
"""

nome = input('Por favor, digite o seu nome: ')
idade = input('Por favor, digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é "{nome}"')
    print(f'Seu nome invertido é: "{nome[::-1]}".')

    if ' ' in nome:
         print(f'Seu nome contém espaços.')
    else:
         print('Seu nome não contém espaços.')
    
    print(f'Seu nome contém {len(nome)} letras.') 
    print(f'A primeira letra do seu nome é "{nome[0]}".')
    print(f'A última letra do seu nome é "{nome[-1]}".')
else:
     print('Desculpe, mas você deixou campos vazios...')