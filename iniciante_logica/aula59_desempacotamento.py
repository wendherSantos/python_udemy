# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    # 0           1
    ["Sarah", "Kelwin"],  # 0
    # 0
    ["Weslley"],  # 1
    # 0           1         2              3
    ["Dori", "Wendher", "Gerson"]  # 2
]

# # a, b, c = lista
# # print(a, c)
# p, b, *_, ap, u = lista
# print(p, u, ap)

# print(*lista)
# print(*string)  
# print(*tupla) 

print(*salas, sep = '\n') 
