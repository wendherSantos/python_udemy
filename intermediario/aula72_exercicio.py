# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def multiplication(*args):
    total = 1
    for number in args:
        total *= number
    return total

result = multiplication(1, 2, 4, 5, 6)
print(result)

# Crie uma funcao fala se um numero é par ou impar
# Retorne se o numero é par ou impar

def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    return 'Odd'

num = float(input('Enter a number: '))
result = even_or_odd(num)
print(f'The number {num} is {result}.')