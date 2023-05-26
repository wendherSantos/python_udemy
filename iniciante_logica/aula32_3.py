"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora (números inteiros) em que você está: ')

if hora.isdigit():
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print(f'Bom dia! Agora são {hora_int} AM')
    elif hora_int >= 12 and hora_int <= 17:
        print(f'Boa tarde! Agora são {hora_int} PM')
    elif hora_int >= 18 and hora_int <= 23:
        print(f'Boa noite! Agora são {hora_int} PM')
    else:
        print(f'Não conheço esse horário.')
else:
    print('Você não digitou um número inteiro...')