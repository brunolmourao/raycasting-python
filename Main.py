""""
Programa onde o loop principal irá executar
"""

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
        for c in range(num_col):
            x_lc = -tam / 2 + var * (1 + 2 * c) / 2
            y_lc = tam / 2 - var * (1 + 2 * l) / 2
            p.append(Point(x_lc, y_lc, z))

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
            lista_colisoes.append([furo, obj, raio.ponto(t)])

# TODO pintar a tela
# Neste laço pintamos uma tela
tela = painel(4, 100, 100)
for pixel in tela:
    pass
