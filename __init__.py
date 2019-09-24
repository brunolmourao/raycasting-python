""""
Programa onde o loop principal irá executar
"""

import sys

from tkinter import *
import utils.constant as constant
from geometricAttributes.Point import Point
from geometricObjects.Cilinder import Cillinder
from geometricObjects.Cone import Cone
from geometricObjects.Cube import Cube
from utils.Panel import Panel, Tela
from utils.Ray import Ray
from light.Lighting import *
from utils.Transform import transform_to_camera
from materials.Material import Material

sys.setrecursionlimit(constant.RECURSION_LIMIT)


def camera_init(obs, lookat, vup):
    kg = obs - lookat
    k = kg / np.linalg.norm(kg)
    vg = vup - obs
    ig = calc.produto_vetorial(vg, k)
    i = ig / np.linalg.norm(ig)
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


# Coordenadas para camera, placa e tela ================================================================================
num_furos = 60  # número de furos por linha. Define a resolução da tela
tamanho = 60  # medida da aresta da placa em unidades de coordenada
viewer = np.array([0, 0, 0])  # Coordeanadas do observador
look_at = np.array([0, 0, -10])  # Ponto q define a direção da camera
v_up = np.array([0, 10, -10])  # Ponto que define o plano sagital

camera = camera_init(viewer, look_at, v_up)
placa = Panel(tamanho, num_furos, num_furos)
tela = Tela(tamanho, num_furos, num_furos)

material1 = Material(1, [0, 1, 1], [0, 0.5, 0.6], [0.6, 0.1, 0])

# CENÁRIO ==============================================================================================================
objects = []
# cube1 = Cube(transform_to_camera(camera, np.array([0, -2, -20])), 6, transform_to_camera(camera, np.array([0, 1, 0])),
# material1)

# cube2 = Cube(transform_to_camera(camera, np.array([0, 4, -20])), 6, transform_to_camera(camera, np.array([0, 1, 0])),
# material1)
# cube3 = Cube(transform_to_camera(camera, np.array([0, 10, -20])), 6, transform_to_camera(camera, np.array([0, 1, 0])),
# material1)

cube1 = Cube(Point(0, -2, -20), 6, Point(0, 1, 0), material1)
cube1.set_cor('1')
cube2 = Cube(Point(0, 4, -20), 6, Point(0, 1, 0), material1)
cube2.set_cor('2')
cube3 = Cube(Point(0, 10, -20), 6, Point(0, 1, 0), material1)
cube3.set_cor('3')
# cone = Cone(Point(0, 0, -10), 2, 5, Point(0, 1, 0))
# cone.set_cor('A')
# cilindro = Cillinder(Point(0, -2, -10), 0.5, 2, Point(0, 1, 0))
# cilindro.set_cor('T')

objects.append(cube1)
objects.append(cube2)
objects.append(cube3)
# objects.append(cone)
# objects.append(cilindro)

# FONTES LUMINOSAS =====================================================================================================
# TODO Definir valores adequados para a iluminação
fontesLuminosas = []
light_amb = EnvironmentLight([1, 1, 1])
light_p1 = PointLight([0, 0, 0], np.array([1, 1, 1]))
light_sp2 = SpotLight([0, 0, 0], np.array([1, 10, 1]), np.array([1, 1, 1]))
light_rmt3 = RemoteLight([0, 0, 0], np.array([1, 1, 0]))

fontesLuminosas.append(light_amb)
# fontesLuminosas.append(light_p1)
# fontesLuminosas.append(light_sp2)
# fontesLuminosas.append(light_rmt3)

# MUDANÇA DE COORDENADAS MUNDO->CAM ====================================================================================
# TODO Implemetar métodos transform_to_camera nos objetos, nas fonte luminosas, na placa e na tela
"""
for o in objects:
    o.transform_to_camera(camera)
for f in fontesLuminosas:
    f.transform_to_camera(camera)
viewer = transform_to_camera(camera, viewer).coords()
placa.transform_to_camera(camera)
tela.transform_to_camera(camera)
"""
# COLISÕES =============================================================================================================
lista_colisoes = []
# TODO Transformei a Placa num objeto, não testei as mudanças
for l in range(len(placa.p)):
    # print("\n")
    for c in range(len(placa.p[l])):
        # print(f"[{l}][{c}]: ", end=" ")
        furo = placa.p[l][c]
        raio = Ray(Point(viewer[0], viewer[1], viewer[2]), furo.coords() - viewer)
        min_t = 999999
        primeiro_obj = None
        for obj in objects:
            intersecoes = obj.intersection_with(raio)
            for t in intersecoes:
                # lista_colisoes.append([furo, obj, raio.ponto(t), t])
                print(f"t = {t}")
                print(f"tmin = {min_t}")
                print(f"cor = {obj.cor}")
                if t < min_t:
                    min_t = t
                    primeiro_obj = obj
            # CASO SEJA NECESSARIO MUDAR ALGUM ATRIBUTO DO OBJETO ATINGIDO, USAR O primeir_obj
            if primeiro_obj:
                tela.set_cor(l, c, primeiro_obj.material, min_t, fontesLuminosas)
                tela.set_simbolo_furo(l, c, primeiro_obj.cor)  # Temporario. Serve para impressão no terminal [REMOVER]

# IMPRESSÃO DE TELA ====================================================================================================
root = Tk()
root.geometry("300x300")
c = Canvas(root, height=300, width=300, bg="blue")

for lin in range(len(tela.p)):
    for col in range(len(tela.p[lin])):
        # print(" [", lin, col, "]", self.__p[lin][col][1], end="")
        if tela.p[lin][col][1] == 'A':
            c.create_line(col, lin, col + 1, lin, fill="green")
        if tela.p[lin][col][1] == 'T':
            c.create_line(col, lin, col + 1, lin, fill="brown")
        if tela.p[lin][col][1] == '1':
            c.create_line(col, lin, col + 1, lin, fill="red")
        if tela.p[lin][col][1] == '2':
            c.create_line(col, lin, col + 1, lin, fill="black")
        if tela.p[lin][col][1] == '3':
            c.create_line(col, lin, col + 1, lin, fill="white")
        print(tela.p[lin][col][1], end="")
    print()
c.pack()
root.mainloop()
