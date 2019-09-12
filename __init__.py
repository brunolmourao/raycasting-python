""""
Programa onde o loop principal irá executar
"""

import sys
from typing import List

import numpy as np
from tkinter import *
import utils.CalcWithVectors as calc
import utils.constant as constant
from geometricAttributes.Point import Point
from geometricObjects.Cilinder import Cillinder
from geometricObjects.Cone import Cone
from geometricObjects.Cube import Cube
from utils.Panel import Panel
from utils.Ray import Ray

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


def camera_init(obs, lookat):
    K = obs - lookat
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


# Coordenadas para camera, placa e tela
num_furos = 60
tamanho = 18
viewer = np.array([0, 0, 0])
look_at = np.array([0, 0, -4])

camera = camera_init(viewer, look_at)
placa = painel_init(tamanho, num_furos, num_furos)
tela = Panel(tamanho, num_furos, num_furos)

# Cenário
objects = []
cube1 = Cube(Point(0, -2, -20), 6, Point(0, 1, 0))
cube1.set_cor('1')
cube2 = Cube(Point(0, 4, -20), 6, Point(0, 1, 0))
cube2.set_cor('2')
cube3 = Cube(Point(0, 10, -20), 6, Point(0, 1, 0))
cube3.set_cor('3')
cone = Cone(Point(0, 0, -10), 2, 5, Point(0, 1, 0))
cone.set_cor('A')
cilindro = Cillinder(Point(0, -2, -10), 0.5, 2, Point(0, 1, 0))
cilindro.set_cor('T')

objects.append(cube1)
objects.append(cube2)
objects.append(cube3)
# objects.append(cone)
# objects.append(cilindro)

lista_colisoes = []
for l in range(len(placa)):
    # print("\n")
    for c in range(len(placa[l])):
        # print(f"[{l}][{c}]: ", end=" ")
        furo = placa[l][c]
        raio = Ray(Point(viewer[0], viewer[1], viewer[2]), furo.coords() - viewer)
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
# pintar tela

root = Tk()
root.geometry("60x60")
c = Canvas(root, height=60, width=60, bg="blue")

for lin in range(len(tela.p)):
    for col in range(len(tela.p[lin])):
        # print(" [", lin, col, "]", self.__p[lin][col][1], end="")
        if tela.p[lin][col][1] == 'A':
            c.create_line(lin, col, lin + 1, col, fill="green")
        if tela.p[lin][col][1] == 'T':
            c.create_line(lin, col, lin + 1, col,  fill="brown")
        if tela.p[lin][col][1] == '1':
            c.create_line(lin, col, lin + 1, col, fill="red")
        if tela.p[lin][col][1] == '2':
            c.create_line(lin, col, lin + 1, col, fill="black")
        if tela.p[lin][col][1] == '3':
            c.create_line(lin, col, lin + 1, col,  fill="white")
        # c.create_line(lin, col, lin, col, width=200, fill="brown")
        print(tela.p[lin][col][1], end="")
    print()
c.pack()
root.mainloop()
# tela.show()
"""
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
            intersecoes = obj.intersection_with(raio)
            for t in intersecoes:
                lista_colisoes.append([furo, obj, raio.ponto(t), t])
                if t < min_t:
                    min_t = t
                    primeiro_obj = obj

        # CASO SEJA NECESSARIO MUDAR ALGUM ATRIBUTO DO OBJETO ATINGIDO, USAR O primeir_obj
        if primeiro_obj:
            tela.set_simbolo_furo(l, c, primeiro_obj.cor)

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
