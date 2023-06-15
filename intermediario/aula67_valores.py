"""
valores padrão para parâmetros
ao definir uma função, os parametros podem ter valores padrao.
Caso o valor nao seja enviado para o parametro, o valor padrao será usado.
Refatorar: editar/melhorar o codigo.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} \n\t Resultado:', x + y + z)
    else:
        print(f'{x=} {y=} \n\t Resultado:', x + y)

soma(12, 12)
soma(111, 12)
soma(11, 12123, 0)
