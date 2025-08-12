"""
CONSTANTE = 'variaveis'  que não vão mudar muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)

"""

velocidade = 62 # velocidade atual do carro 
local_carro = 101 # local em que o carro está na estrada 

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está 
RADAR_RANGE = 1 # a distância onde o radar pega 

velo_car_pass_radar1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >=(LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar_1 and velo_car_pass_radar1

if velo_car_pass_radar1 :
    print ('velocidade carro passou do radar 1')

if carro_multado_radar1 :
    print ('Carro passou radar 1')

if carro_multado_radar1 :
    print ('Carro multado em radar 1')