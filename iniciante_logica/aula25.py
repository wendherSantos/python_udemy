"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)

"""

nome = 'Wendher'
preco = 1000.12412
variavel = '%s, preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X %08X' % (1645, 1235, 2123))