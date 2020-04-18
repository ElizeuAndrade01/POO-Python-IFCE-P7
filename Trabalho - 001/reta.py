import math
class Reta:
    def __init__(self, p1y, p1x, p2y, p2x):

        ab = (p1x-p2x)**2 + (p1y-p2y)**2
        distAB = math.sqrt(ab)
        print('A distância entre esses dois pontos é de:', float(distAB), 'unidades de medida')
