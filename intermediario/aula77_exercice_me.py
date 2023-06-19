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
        'Resposta': '2',
    },
    { 
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['1', '2', '3', '5'],
        'Resposta': '4',
    },
]

qtd_perguntas = len(perguntas)
resposta_correta = 0
resposta_incorreta = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for index, opcao in enumerate(pergunta['Opções']):
        print(f'{index + 1}) {opcao}')
    resposta = input('Digite o número da resposta correta: ')
    if resposta == pergunta['Resposta']:
        print('Resposta Correta! 👍\n')  
        resposta_correta += 1
    else:
        print('Resposta Incorreta! 😭\n')
        resposta_incorreta += 1

if resposta_correta == qtd_perguntas: 
    print(f'PARABÉNS! VOCÊ ACERTOU {resposta_correta} de {qtd_perguntas} perguntas! 😱👌')
else:
    print(f'Você acertou {resposta_correta} de {qtd_perguntas} perguntas!')

