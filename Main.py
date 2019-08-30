""""
Programa onde o loop principal irá executar
"""

from objetos.Cilinder import Cillinder
from objetos.Cone import Cone
from objetos.Cube import Cube
from objetos.Point import Point
from objetos.Ray import Ray

z = 55  # posição da placa perfurada


# TODO: escrever as coordenadas dos furos (onde esta x e y)
def painel(tam, num_linhas):
    """O centro do painel tem coordenada [0,0,z]
        deste modo os vertices tem coord:
        [-tam/2, tam/2, z]  ______ [tam/2,  tam/2, z]
                           |  .  |
        [-tam/2,-tam/2, z] |_____| [tam/2, -tam/2, z]
    """
    p = []
    for i in range(num_linhas):
        p.append([x, y, posicao] * num_linhas)
    return p


"""poi[i]][j] = [-tam/2, tam/2, z]

00 01 02 03 04 ... 0L
10 11 12 13 14 ... 1L
20 21 22 23 24 ... 2L
|  |  |  |  |   \  |
L0 L1 L2 L3 L4 ... LL

x = tam/2
IJ = [-x + tam/L*j, x - tam/L*i, z]
"""



# Cenário
objects = []

cube1 = Cube(Point(0, 0, 5), 10, Point(0, 1, 0))
cube2 = Cube(Point(0, 10, 5), 10, Point(0, 1, 0))
cube3 = Cube(Point(0, 20, 5), 10, Point(0, 1, 0))
cone = Cone(Point(0, 10, 30), Point(0, 1, 0), 20, 5)
cilinder = Cillinder(Point(0, 0, 30), 2, 10, Point(0, 1, 0))

objects.append(cube1)
objects.append(cube2)
objects.append(cube3)
objects.append(cone)
objects.append(cilinder)

obs = Ponto(0, 0, 70)
placa = painel(20, 100)

# Nesse laço o raio fura todos os objetos
for furo in placa:
    raio = Ray(obs, furo)
    for obj in objects:
        t = obj.intersection_with(raio)
        # falta verificar se t é vazio
        print(obj, obj.ponto(t))
