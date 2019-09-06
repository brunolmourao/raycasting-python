""""
Programa onde o loop principal irá executar
"""
#attributes
from geometricAttributes.Point import Point

#objects
from geometricObjects.Cilinder import Cillinder
from geometricObjects.Cone import Cone
from geometricObjects.Cube import Cube

#utils
from utils.Ray import Ray
from utils.constant import POSICAO_PLACA_Z


def painel(tam, num_lin, num_col):
    """O centro do painel tem coordenada [0,0,POSICAO_PLACA_Z]
        deste modo os vertices tem coord:
        [-tam/2, tam/2, POSICAO_PLACA_Z]  ______ [tam/2,  tam/2, POSICAO_PLACA_Z]
                           |  .  |
        [-tam/2,-tam/2, POSICAO_PLACA_Z] |_____| [tam/2, -tam/2, POSICAO_PLACA_Z]
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
            p.append(Point(x_lc, y_lc, POSICAO_PLACA_Z))

    return p


########## 
# Cenário
#########

#list of objects
objects = []

#cubes
cube_1 = Cube(Point(0, -2, -20), 6, Point(0, 1, 0))
cube_2 = Cube(Point(0, 4, -20), 6, Point(0, 1, 0))
cube_3 = Cube(Point(0, 10, -20), 6, Point(0, 1, 0))

#cones
cone = Cone(Point(0, 0, -10), 3, 8, Point(0, 1, 0))

#cilinders
cilinder = Cillinder(Point(0, -2, -10), 0.5, 8, Point(0, 1, 0))

#adding objects
objects.append(cube_1)
objects.append(cube_2)
objects.append(cube_3)
objects.append(cone)
objects.append(cilinder)

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

print(lista_colisoes)            

# TODO pintar a tela
# Neste laço pintamos uma tela
tela = painel(4, 100, 100)

for pixel in tela:
    pass
