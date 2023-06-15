"""
argumntos nomeados e nao nomeados em funcoes python
argumento nomeado tem nome com sinal de igual
argumento nao nomeado recebe apenas o argumento (valor)
"""
# definicao
def soma(x, y, z):
    print(f'{x=} y={y} z={z}| x + y = {x + y + z}')
    
soma(1, 2, 3)
soma(y=2, x=1, z=4)
soma(1, 2, z=5)

