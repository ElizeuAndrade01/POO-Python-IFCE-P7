class Ponto:
    def __init__(self , x, y, n):
        if x > 0 and y > 0:
            print("O ponto", n ,"está no quadrante 1.")
        if x < 0 and y > 0:
            print("O ponto", n ,"está no quadrante 2.")
        if x < 0 and y < 0:
            print("O ponto", n ,"está no quadrante 3.")
        if x > 0 and y < 0:
            print("O ponto", n ,"está no quadrante 4.")
        if x == 0 and y == 0:
            print("O ponto", n ,"está no ponto 0")

