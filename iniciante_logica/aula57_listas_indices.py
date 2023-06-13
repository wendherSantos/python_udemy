"""
Listas de listas e seus índices
"""
salas = [
    # 0           1
    ["Sarah", "Kelwin"],  # 0
    # 0
    ["Weslley"],  # 1
    # 0           1         2              3
    ["Dori", "Wendher", "Gerson"]  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'\nA sala é {sala}')
    for aluno in sala:
        print(aluno)
