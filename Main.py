""""
Programa onde o loop principal irá executar
"""
from typing import List

from estruturaDeDados.Point import Point
from objetos.Cilinder import Cillinder
from objetos.Cone import Cone
from objetos.Cube import Cube
from objetos.Ray import Ray

z = -4  # posição da placa perfurada


def painel(tam, num_lin, num_col):
    """O centro do painel tem coordenada [0,0,z]
        deste modo os vertices tem coord:
        [-tam/2, tam/2, z]  ______ [tam/2,  tam/2, z]
                           |  .  |
        [-tam/2,-tam/2, z] |_____| [tam/2, -tam/2, z]
    """
    p = []
    if tam / num_lin >= tam / num_col:
        var = tam / num_col
    else:
        var = tam / num_lin

    for l in range(num_lin):
        p_linha: List[Point] = []
        for c in range(num_col):
            x_lc = -tam / 2 + var * (1 + 2 * c) / 2
            y_lc = tam / 2 - var * (1 + 2 * l) / 2
            p_linha.append(Point(x_lc, y_lc, 4))
        p.append(p_linha)
    return p


# Cenário
objects = []

cube1 = Cube(Point(0, -2, -20), 6, Point(0, 1, 0))
cube2 = Cube(Point(0, 4, -20), 6, Point(0, 1, 0))
cube3 = Cube(Point(0, 10, -20), 6, Point(0, 1, 0))
cone = Cone(Point(0, 0, -10), 3, 8, Point(0, 1, 0))
cilindro = Cillinder(Point(0, -2, -10), 0.5, 8, Point(0, 1, 0))

objects.append(cube1)
objects.append(cube2)
objects.append(cube3)
objects.append(cone)
objects.append(cilindro)

obs = Point(0, 0, 0)
placa = painel(4, 100, 100)

# Nesse laço o raio fura todos os objetos
lista_colisoes = []
for furo in placa:
    raio = Ray(obs, furo)
    for obj in objects:
        intersecoes = obj.intersection_with(raio)
        for t in intersecoes:
            lista_colisoes.append([furo, obj, raio.ponto(t), t])

# TODO pintar a tela
# Neste laço pintamos uma tela
tela = painel(4, 100, 100)
for i in range(len(tela)):
    for j in range(len(tela)):
        # BUSCA EM LISTA_COLISOES
        letra = '.'
        val = []
        for k in range(1):
            val.append(tela[i][j], letra)
        tela.__setitem__(i, val)

    # imprimi
    if pixel in lista_colisoes:
        if lista_colisoes[pixel][1] == cube1:
            print("0")
        elif lista_colisoes[pixel][1] == cube2:
            print("X")
        elif lista_colisoes[pixel][1] == cube3:
            print("1")
        elif lista_colisoes[pixel][1] == cone:
            print("A")
        elif lista_colisoes[pixel][1] == cilindro:
            print("T")
        else:
            print(".")

"""
........................................................................................................
........................................................................................................
........................................................................................................
..........................................A......................000000000000...........................
.........................................AAA.....................000000000000...........................
........................................AAAAA....................000000000000...........................
.......................................AAAAAAA...................000000000000...........................
......................................AAAAAAAAA..................000000000000...........................
.....................................AAAAAAAAAAA.................XXXXXXXXXXXX...........................
....................................AAAAAAAAAAAAA................XXXXXXXXXXXX...........................
...................................AAAAAAAAAAAAAAA...............XXXXXXXXXXXX...........................
..................................AAAAAAAAAAAAAAAAA..............XXXXXXXXXXXX...........................
.................................AAAAAAAAAAAAAAAAAAA.............XXXXXXXXXXXX...........................
................................AAAAAAAAAAAAAAAAAAAAA............111111111111...........................
........................................TTTT.....................111111111111...........................
........................................TTTT.....................111111111111...........................
........................................TTTT.....................111111111111...........................
........................................TTTT.....................111111111111...........................
........................................................................................................
........................................................................................................
........................................................................................................
........................................................................................................
"""
