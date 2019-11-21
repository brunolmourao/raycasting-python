import sys

from DataStructure.Point import Point
from Object.Cone import Cone
from Object.Cube import Cube
from Object.Cylinder import Cylinder
from Object.Sphere import Sphere
from utils.Material import Material
from utils.Panel import Panel
from utils.Ray import Ray
from utils.Utils import camera_init_
from utils.constants import RECURSION_LIMIT

"""
==================================================================
UNIVERSIDADE FEDERAL DO CEARÁ
COMPUTAÇÃO GRÁFICA
TRABALHO 1 -
------------------------------------------------------------------
Autores: 354037 Alysson Macedo
         000000 
         000000
         000000
         000000
         000000 
==================================================================
"""

sys.setrecursionlimit(RECURSION_LIMIT)

# Posicionamento da Placa furada =================================
num_furos = 100  # número de furos por linha. Define a resolução da tela
tamanho = 10  # medida da aresta da placa em unidades de coordenada
placa = Panel(tamanho, num_furos, num_furos)
"""O centro do painel tem coordenada [0,0,z]
    deste modo os vertices tem coord:
    [-tam/2, tam/2, z]  ______ [tam/2,  tam/2, z]
                       |  .  |
    [-tam/2,-tam/2, z] |_____| [tam/2, -tam/2, z]
"""

# Posicionamento de Câmera =======================================
viewer = Point(0, 0, 0)  # Coordeanadas do observador
look_at = Point(0, 0, -10)  # Ponto q define a direção da camera
view_up = Point(0, 10, -10)  # Ponto que define o plano sagital
camera = camera_init_(viewer.coord, look_at.coord, view_up.coord)

# Todo: é esperado que com os dados acima camera seja a matriz identidade?
print(camera)

# CENÁRIO ========================================================

mat_teste = Material(0, 0, 0)
objetos = []

cubo1 = Cube(Point(0, -2, -20), Point(0, 1, 0).coord, 6, mat_teste, "1")
cubo2 = Cube(Point(0, 4, -20), Point(0, 1, 0).coord, 6, mat_teste, "2")
cubo3 = Cube(Point(0, 10, -20), Point(0, 1, 0).coord, 6, mat_teste, "3")
cone = Cone(Point(0, 0, -10), Point(0, 1, 0).coord, 2, 6, mat_teste, "_")
cilindro = Cylinder(Point(0, -2, -10), Point(0, 1, 0).coord, 0.5, 2, mat_teste, "H")
esfera = Sphere(Point(0, 6.5, -10), 0.5, mat_teste, "o")

objetos.append(cubo1)
objetos.append(cubo2)
objetos.append(cubo3)
objetos.append(cone)
objetos.append(cilindro)
objetos.append(esfera)

# FONTES LUMINOSAS ===============================================
fontes_luminosas = []
# luz_ambiente =
# fontes_luminosas.append(luz_ambiente)

# MUDANÇAS DE COORDENADAS MUNDO -> CAM ===========================
for o in objetos:
    o.transforme_coord_to_(camera)
for f in fontes_luminosas:
    f.transforme_coord_to_(camera)

# COLISÕES =======================================================
for l in range(len(placa.matrix_pixel)):
    for c in range(len(placa.matrix_pixel[l])):
        print(l, c)
        furo = placa.get_p(l, c)
        raio = Ray(viewer, furo.coord - viewer.coord)
        t_min = 99999999
        primeiro_objeto = None
        for obj in objetos:
            t = obj.intersection_with(raio)
            if t:
                if t < t_min:
                    t_min = t
                    primeiro_obj = obj
                    placa.set_cor(l, c, obj.cor)  # temporario.
                    # placa.set_cor(l, c, calcula_cor(obj, fontes_luminosas))
# EXIBIÇÃO EM TELA ===============================================
placa.show()

"""
# ===============
a = Point(0, 1, 2)
b = Point(1, 3, 2)
c = Point(5, 2, 8)

v1 = Vector(a, b)
v2 = Vector(b, c)
v3 = Vector(c, a)

f1 = Face(a, b, c)
v = Vector(Point(0, 0, 0), a)
r = Ray(c, v.coord)

plano = Plane(b, v1.coord)
esfera = Sphere(b, 10)
cilindro = Cylinder(a, v1.coord, 10, 30)
cone = Cone(a, v1.coord, 10, 30)

print(a.coord, b.coord, c.coord)
print(v1.coord, v2.coord, v3.coord)
# print(f1.normal_vector)

# print("v: ", v)
# print(v1.coord)# https://www.wolframalpha.com/input/?i=plane+through+point+%281%2C3%2C2%29+with+normal+vector+%281%2Fsqrt+5%2C+2%2F+sqrt+5%2C0%29
# print(v.coord) # https://www.wolframalpha.com/input/?i=line+through+%285%2C2%2C8%29+and+vector+%280%2C1%2Fsqrt5%2C2%2Fsqrt5%29
# print(plano.n)
# print(r.d)

# print(plano.intersection_with(r))
# print(r.get_point(plano.intersection_with(r)).coord)

# print(esfera.intersection_with(r)) # https://www.wolframalpha.com/input/?i=sphere+center+%281%2C3%2C2%29+radius10
# print(r.get_point(esfera.intersection_with(r)).coord) #https://www.wolframalpha.com/input/?i=x%3D5%2C+z%3D2k%2B8%2Cy%3Dk%2B2%2C+%28y-3%29%5E2%2B%28z-2%29%5E2+%3D+84

print("========")

# print(cilindro.intersection_with(r)) # https://www.wolframalpha.com/input/?i=cylinder+center+%285%2C2%2C8%29+radius10%2C+height30+with+normal+vector+%281%2Fsqrt+5%2C+2%2F+sqrt+5%2C0%29
# print("final: ", r.get_point(cilindro.intersection_with(r)).coord)

# print("final: ", r.get_point(cone.intersection_with(r)).coord)

cubo = Cube(a, Point(0, 1, 0).coord, 10)
for i in cubo.lista_vertices:
    print(i.label, " - ", i.coord)
for i in cubo.lista_aresta:
    print(i.label, " - ", i.s.label, "\t", i.d.label)
for i in cubo.lista_faces:
    print(i.label, " - ", i.normal_vector)

print("cubo final", r.get_point(cubo.intersection_with(r)).coord)
"""
