"""
Flag (bandeira) - marcar um local
none = nao valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('NÃO faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
