"""
Closure e funcoes que retornam outras funcoes
"""

def create_salutation(salutation):
    def salute(name):
        return f'{salutation}, {name}!'
    return salute

falar_bom_dia = create_salutation('Bom dia')
falar_boa_noite = create_salutation('Boa noite')

for nome in ['Maria', 'Joana', 'Wendher']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
