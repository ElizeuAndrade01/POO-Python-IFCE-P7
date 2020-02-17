import math
import ponto

def reta(p1x, p1y, p2x, p2y):

    distAB = math.sqrt((p1x-p2y)**2) + ((p2x-p2y)**2)
    print('A distância entre esses dois pontos é de:', distAB, 'unidades de medida')
