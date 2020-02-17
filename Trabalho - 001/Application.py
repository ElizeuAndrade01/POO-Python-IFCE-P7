import math
import ponto
import reta

p1x = input ('Digite o x do seu ponto 1: ')
p1y = input ('Digite o y do seu ponto 1: ')

p2x = input ('Digite o x do seu ponto 2: ')
p2y = input ('Digite o y do seu ponto 2: ')


funcPonto = ponto.ponto

funcReta = reta.reta

funcPonto(int(p1x), int(p1y), 1)
funcPonto(int(p2x), int(p2y), 2)
funcReta(int(p1x), int(p1y), int(p2x), int(p2x))

