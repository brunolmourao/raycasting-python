""""
Programa onde o loop principal irá executar
"""

import sys
from typing import List

import numpy as np
import math

import utils.CalcWithVectors as calc
from geometricAttributes.Point import Point
from geometricObjects.Cone import Cone
from geometricObjects.Cube import Cube

from utils.Panel import Panel
from utils.Ray import Ray

import utils.constant as constant

sys.setrecursionlimit(constant.RECURSION_LIMIT)


def painel_init(tam, num_lin, num_col):
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
            p_linha.append(Point(x_lc, y_lc, constant.POSICAO_PLACA_Z))
        p.append(p_linha)
    return p


def camera_init(o, lat):
    obs = np.array(o)
    look_at = np.array(lat)
    K = obs - look_at
    k = calc.normalizar(K)
    vup = np.array([0, 10, -4])
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


# Coordenadas para camera e placa
tam_placa = 18
p_obs = [0, 0, 0]
p_look_at = [0, 0, -4]
camera = camera_init(p_obs, p_look_at)
placa = painel_init(4, tam_placa, tam_placa)

# Cenário
objects = []
cube1 = Cube(Point(0, -2, -20), 6, Point(0, 1, 0))
cube1.set_cor('1')
# print(f" teste {cube1.intersection_with(Ray(Point(0,0,0),Point(3,-2,-17)))}")
cube2 = Cube(Point(0, 4, -20), 6, Point(0, 1, 0))
cube2.set_cor('2')
# cube2 = Cube(calc.transform_camera(camera, Point(0, 4, -20)), 6, calc.transform_camera(camera, Point(0, 1,
# 0))) cube2.set_cor('2') cube3 = Cube(calc.transform_camera(camera, Point(0, 10, -20)), 6, calc.transform_camera(
# camera, Point(0, 1, 0))) cube3.set_cor('3') cone = Cone(calc.transform_camera(camera, Point(0, 0, -10)), 3, 8,
# calc.transform_camera(camera, Point(0, 1, 0))) cilindro = Cillinder(calc.transform_camera(camera, Point(0, -2,
# -10)), 0.5, 2, calc.transform_camera(camera, Point(0, 1, 0)))
objects.append(cube1)
objects.append(cube2)
# objects.append(cube3)
# objects.append(cone)
# objects.append(cilindro)
obs_array = np.array(p_obs)
lista_colisoes = []
tela = Panel(6, tam_placa, tam_placa)
for l in range(len(placa)):
    for c in range(len(placa[l])):
        furo = placa[l][c]
        raio = Ray(Point(p_obs[0], p_obs[1], p_obs[2]), furo.coords() - obs_array)
        min_t = 999999
        primeiro_obj = None
        for obj in objects:
            intersecoes = obj.intersection_with(raio)
            for t in intersecoes:
                lista_colisoes.append([furo, obj, raio.ponto(t), t])
                if t < min_t:
                    min_t = t
                    primeiro_obj = obj
                # CASO SEJA NECESSARIO MUDAR ALGUM ATRIBUTO DO OBJETO ATINGIDO, USAR O primeir_obj
            if primeiro_obj:
                tela.set_simbolo_furo(l, c, primeiro_obj.cor)
            #print(f" l = {l} c= {c} , min_t = {min_t}")
            #print("\n")
# pintar tela
tela.show()
"""
# lista_colisoes: List[List[Union[Union[Point, Union[Cube, Cone, Cillinder], Point, float], Any]]]
tela: List[List[Point, str, Point]]
# furo: Point
# obj: Union[Cube, Cone, Cillinder]
# t: float

# Calcula lista de colisões com os objetos, qual o primeiro objeto e o t do ponto atingido
lista_colisoes = []
tela = Panel(6, tam_placa, tam_placa)
count = 1
for l in range(len(placa)):
    for c in range(len(placa[l])):
        furo = placa[l][c]
        raio = Ray(Point(p_obs[0], p_obs[1], p_obs[2]), furo.coords())
        min_t = 999999999999
        primeiro_obj = None
        for obj in objects:
            # print(f"----------------------------------------------->{obj}")
            intersecoes = obj.intersection_with(raio)
            for t in intersecoes:
                lista_colisoes.append([furo, obj, raio.ponto(t), t])
                # print(f"tint  = {t}")
                if t < min_t:
                    # print(f"c = {count}")
                    count = count + 1
                    # print(f"min_t{min_t}")
                    min_t = t
                    # print(f"min_taf{min_t}")
                    primeiro_obj = obj

        # CASO SEJA NECESSARIO MUDAR ALGUM ATRIBUTO DO OBJETO ATINGIDO, USAR O primeir_obj
        if primeiro_obj:
            tela.set_simbolo_furo(l, c, primeiro_obj.cor)
            tela.set_t_furo(l, c, raio.ponto(min_t))
        print(f" l = {l} c= {c} , min_t = {min_t}")
print("\n")
# pintar tela
tela.show()
"""
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
"""
