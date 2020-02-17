import math
import ponto
import reta

p1x = input ('Digite o x do seu ponto 1: ')
p1y = input ('Digite o y do seu ponto 1: ')

p2x = input ('Digite o x do seu ponto 2: ')
p2y = input ('Digite o y do seu ponto 2: ')

#p1x = -13
#p1y = 14
#p2x = 13
#p2y = 19

funcPonto = ponto.ponto

funcReta = reta.reta

funcPonto(float(p1x), float(p1y), 1)
funcPonto(float(p2x), float(p2y), 2)

funcReta(float(p1y),float(p1x),float(p2y),float(p2x))

