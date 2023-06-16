"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
        
soma1 = soma(1, 2, 3)
print(soma1)

soma2 = soma(5, 2, 1)
print(soma2)

numeros = 5, 2, 1, 4, 2, 2
soma3 = soma(*numeros)
print(soma3)

print(sum(numeros))