"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou') 

numero = 0

while numero < 100:
    numero += 1

    if numero == 2:
        print(f'Não vou mostrar o', numero)
        continue

    if numero >= 10 and numero <= 99:
        print(f'Não vou mostrar o', numero)
        continue

    print(numero)

print('Acabou mano')