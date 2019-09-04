""""
Programa onde o loop principal irá executar
"""
from typing import List
import auxiliar.CalcWithVectors as calc
from estruturaDeDados.Point import Point
from objetos.Cilinder import Cillinder
from objetos.Cone import Cone
from objetos.Cube import Cube
from objetos.Ray import Ray
import numpy as np

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


obs = np.array([30,4,0])
look_at = np.array([7,5,0])
K = obs - look_at
k = calc.normalizar(K)
vup = np.array([7,10,0])
V = vup - obs
I = calc.produto_vetorial(V,k)
i = calc.normalizar(I)
j = calc.produto_vetorial(k,i)
i = np.append(i,[0])
j = np.append(j,[0])
k = np.append(k,[0])
obs = np.append(obs,[1])
camera = i
camera = np.vstack((camera,j))
camera = np.vstack((camera,k))
camera = np.vstack((camera,obs))
camera = np.transpose(camera)
placa = painel(4, 100, 100)

# Cenário
objects = []

cube1 = Cube(calc.transform_camera(camera,Point(0, -2, -20)), 6, calc.transform_camera(camera,Point(0, 1, 0)))
cube2 = Cube(calc.transform_camera(camera,Point(0, 4, -20)), 6, calc.transform_camera(camera,Point(0, 1, 0)))
cube3 = Cube(calc.transform_camera(camera,Point(0, 10, -20)), 6, calc.transform_camera(camera,Point(0, 1, 0)))
cone = Cone(calc.transform_camera(camera,Point(0, 0, -10)), 3, 8, calc.transform_camera(camera,Point(0, 1, 0)))
cone = Cone(calc.transform_camera(camera,Point(0, 0, -10)), 3, 8, calc.transform_camera(camera,Point(0, 1, 0)))
cilindro = Cillinder(calc.transform_camera(camera,Point(0, -2, -10)), 0.5, 8, calc.transform_camera(camera,Point(0, 1, 0)))

objects.append(cube1)
objects.append(cube2)
objects.append(cube3)
objects.append(cone)
objects.append(cilindro)


# Nesse laço o raio fura todos os objetos
lista_colisoes = []
for furo in placa:
    raio = Ray(obs, furo)
    for obj in objects:
        intersecoes = obj.intersection_with(obj, raio)
        for t in intersecoes:
            lista_colisoes.append([furo, obj, raio.ponto(t), t])


""""
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
