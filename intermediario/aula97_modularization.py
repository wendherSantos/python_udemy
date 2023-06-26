# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys
sys.path.append('/home')

import aula97_modulo
from aula97_modulo import variavel_modulo, soma

# print('Este modulo se chama', __name__)
# print(*sys.path, sep='\n')
print(aula97_modulo.variavel_modulo)
print(variavel_modulo)
print(aula97_modulo.soma(2, 3))
print(soma(4, 5))