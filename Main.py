""""
Programa onde o loop principal irá executar
"""

import sys
from typing import List

import numpy as np
import math

import auxiliar.CalcWithVectors as calc
from estruturaDeDados.Point import Point
from objetos.Cilinder import Cillinder
from objetos.Cone import Cone
from objetos.Cube import Cube
from objetos.Panel import Panel
from objetos.Ray import Ray

sys.setrecursionlimit(100)
z = -4  # posição da placa perfurada


def painel_initt(tam, num_lin, num_col):
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

    for lin in range(num_lin):
        p_linha: List[Point] = []
        for col in range(num_col):
            x_lc = -tam / 2 + var * (1 + 2 * col) / 2
            y_lc = tam / 2 - var * (1 + 2 * lin) / 2
            p_linha.append(Point(x_lc, y_lc, 4))
        p.append(p_linha)
    return p


def camera_initt(o, lat):
    obs = np.array(o)
    look_at = np.array(lat)
    K = obs - look_at
    k = calc.normalizar(K)
    vup = np.array([7, 10, 0])
    V = vup - obs
    I = calc.produto_vetorial(V, k)
    i = calc.normalizar(I)
    j = calc.produto_vetorial(k, i)
    i = np.append(i, [0])
    j = np.append(j, [0])
    k = np.append(k, [0])
    obs = np.append(obs, [1])
    cam = i
    cam = np.vstack((cam, j))
    cam = np.vstack((cam, k))
    cam = np.vstack((cam, obs))
    cam = np.transpose(cam)
    return cam


def search(lista, valor):
    for i, sublista in enumerate(lista):
        yield from ((i, j) for j, item in enumerate(sublista) if item == valor)


def is_nan(x):
    return (x is np.nan or x != x)

# Coordenadas para camera e placa
p_obs = [30, 4, 0]
Point(30, 4, 0)
p_look_at = [7, 5, 0]
camera = camera_initt(p_obs, p_look_at)
placa = painel_initt(4, 100, 100)

# Cenário
objects = []
cube1 = Cube(calc.transform_camera(camera, Point(0, -2, -20)), 6, calc.transform_camera(camera, Point(0, 1, 0)))
#cube2 = Cube(calc.transform_camera(camera, Point(0, 4, -20)), 6, calc.transform_camera(camera, Point(0, 1, 0)))
#cube3 = Cube(calc.transform_camera(camera, Point(0, 10, -20)), 6, calc.transform_camera(camera, Point(0, 1, 0)))
#cone = Cone(calc.transform_camera(camera, Point(0, 0, -10)), 3, 8, calc.transform_camera(camera, Point(0, 1, 0)))
#cilindro = Cillinder(calc.transform_camera(camera, Point(0, -2, -10)), 0.5, 8, calc.transform_camera(camera, Point(0, 1, 0)))

objects.append(cube1)
#objects.append(cube2)
#objects.append(cube3)
#objects.append(cone)
#objects.append(cilindro)

"""
# lista_colisoes: List[List[Union[Union[Point, Union[Cube, Cone, Cillinder], Point, float], Any]]]
tela: List[List[Point, str, Point]]
# furo: Point
# obj: Union[Cube, Cone, Cillinder]
# t: float
"""
# Calcula lista de colisões com os objetos, qual o primeiro objeto e o t do ponto atingido
lista_colisoes = []
tela = Panel(4, 100, 100)

for l in range(len(placa)):
    for c in range(len(placa[l])):
        tela.set_simbolo_furo(l, c, '0')
        furo = placa[l][c]
        raio = Ray(Point(30, 4, 0), furo)
        min_t = 999999999999
        primeiro_obj = None
        for obj in objects:
            intersecoes = obj.intersection_with(raio)
            for t in intersecoes:
                if(not is_nan(t)):
                    lista_colisoes.append([furo, obj, raio.ponto(t), t])
                    if t < min_t:
                         min_t = t
                         primeiro_obj = obj

        # CASO SEJA NECESSARIO MUDAR ALGUM ATRIBUTO DO OBJETO ATINGIDO, USAR O primeir_obj
        #print('::', l, c, primeiro_obj.cor)
        tela.set_simbolo_furo(l, c, primeiro_obj.cor)
        tela.set_t_furo(l, c, raio.ponto(min_t))

# pintar tela
tela.show()
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
