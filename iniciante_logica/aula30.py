"""
CONSTANTE = "Variáveis" que não vai mudar
Muitas condicoes no mesmno if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 62 # Velocidade atual do carro
local_carro = 101 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

if  carro_passou_radar_1:
    print('carro multado em radar 1')