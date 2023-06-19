# Exercicio - sistema de perguntas e respostas

perguntas = [
    { 
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': '4',
    },
    { 
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['15', '25', '30', '40'],
        'Resposta': '25',
    },
    { 
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['1', '2', '3', '5'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou! 👍')
    else:
        print('Errou! ❌')

    print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)}.')