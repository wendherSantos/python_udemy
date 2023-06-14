"""
faça uma lista de compras com listas
o usuario deve ter a possibilidade de inserir, apagar e listar valores da sua lista
não permita que o programa quebre com erros de índices inexistentes na lista
"""

lista_compras = []  # Inicializa uma lista vazia para armazenar os itens da lista de compras

while True:
    opcao = input('\nSelecione uma opção: \n'
                '[I] Inserir \n'
                '[A] Apagar \n'
                '[L] Listar \n\n'
                )[0].upper()  # Obtém a opção selecionada pelo usuário, convertendo-a para maiúscula

    if opcao == 'I':  # Se a opção for 'I' (Inserir)
        item = input("\nDigite o item que deseja adicionar à lista: ")  # Solicita ao usuário que digite o item a ser adicionado
        lista_compras.append(item)  # Adiciona o item à lista de compras

    elif opcao == 'A':  # Se a opção for 'A' (Apagar)
        try:
            indice = int(input('Digite o índice a ser deletado: '))  # Solicita ao usuário que digite o índice a ser deletado
            if 0 <= indice < len(lista_compras):  # Verifica se o índice é válido (dentro dos limites da lista de compras)
                del lista_compras[indice]  # Remove o item da lista de compras no índice especificado
            else:
                print('Índice inválido')  # Exibe uma mensagem de erro caso o índice seja inválido
        except ValueError:
            print('Índice inválido')  # Exibe uma mensagem de erro caso o valor digitado não seja um número válido

    elif opcao == 'L':  # Se a opção for 'L' (Listar)
        print('Lista:')
        for indice, item in enumerate(lista_compras):  # Percorre a lista de compras e obtém o índice e o item correspondente
            print(f'\t{indice}, {item}')  # Exibe o índice e o item da lista formatados

    else:
        print('Opção inválida. Digite "I" ou "A" ou "L".')  # Exibe uma mensagem de erro caso a opção seja inválida