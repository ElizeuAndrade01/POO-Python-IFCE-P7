import math
from ponto import Ponto
from reta import Reta

ponto = Ponto
reta = Reta



p1x = input ('Digite o x do seu ponto 1: ')
p1y = input ('Digite o y do seu ponto 1: ')

p2x = input ('Digite o x do seu ponto 2: ')
p2y = input ('Digite o y do seu ponto 2: ')

#p1x = -13
#p1y = 14
#p2x = 13
#p2y = 19

funcPonto = ponto.__init__

funcReta = reta.__init__

funcPonto(ponto ,float(p1x), float(p1y), 1)
funcPonto(ponto ,float(p2x), float(p2y), 2)

funcReta(reta ,float(p1y),float(p1x),float(p2y),float(p2x))

