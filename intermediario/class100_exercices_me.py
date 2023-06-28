import copy

# copy, sorted, produtos.sort
# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print('===========Exercício 1===========')
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] *= 1.10
    produto['preco'] = round(produto['preco'], 2)
    print(produto)
    
print()

print('===========Exercício 2===========')
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda x: x['nome'], reverse=True)

for produto in produtos_ordenados_por_nome:
    print(produto)

print()

print('===========Exercício 3===========')
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda x: x['preco'])

for produto in produtos_ordenados_por_preco:
    print(produto)

print()
