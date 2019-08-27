""""
Programa onde o loop principal irá executar
"""

from objetos.Cilinder import Cillinder
from objetos.Cone import Cone
from objetos.Cube import Cube
from objetos.Point import Ponto
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
objetos = []
cb1 = Cube(Ponto(0, 0, 5), 10, Ponto(0, 1, 0))
cb2 = Cube(Ponto(0, 10, 5), 10, Ponto(0, 1, 0))
cb3 = Cube(Ponto(0, 20, 5), 10, Ponto(0, 1, 0))
cn = Cone(Ponto(0, 10, 30), Ponto(0, 1, 0), 20, 5)
cl = Cillinder(Ponto(0, 0, 30), 2, 10, Ponto(0, 1, 0))
objetos.append(cb1)
objetos.append(cb2)
objetos.append(cb3)
objetos.append(cn)
objetos.append(cl)

obs = Ponto(0, 0, 70)
placa = painel(20, 100)

# Nesse laço o raio fura todos os objetos
for furo in placa:
    raio = Ray(obs, furo)
    for obj in objetos:
        t = obj.intersection_with(raio)
        # falta verificar se t é vazio
        print(obj, obj.ponto(t))
