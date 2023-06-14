"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
= Força o sinal a aparecer antes dos zeros
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}.')
print(f'{variable: <10}.')
print(f'{variable: ^10}.')
print(f'{10000.245231321:0=+10,.1f}.')
print(f'O hexadecimal de 1500 é {1500:08X}')
