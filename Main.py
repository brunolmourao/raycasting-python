""""
Programa onde o loop principal irá executar
"""

from objetos.Cilinder import Cillinder
from objetos.Cone import Cone
from objetos.Cube import Cube
from objetos.Point import Ponto
from objetos.Ray import Ray


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
        p.append([x, y, 500] * num_linhas)
    return p


# Cenário
# TODO: calcular na mão os parâmetros de entrada dos objetos, de modo a posiciona-los corretamente no cenario
objetos = []
cb1 = Cube()
cb2 = Cube()
cb3 = Cube()
cn = Cone()
cl = Cillinder()
objetos.append(cb1)
objetos.append(cb2)
objetos.append(cb3)
objetos.append(cn)
objetos.append(cl)

obs = Ponto(0, 0, z)
placa = painel(100, 100)

# Nesse laço o raio fura todos os objetos
for furo in placa:
    raio = Ray(obs, furo)
    for obj in objetos:
        t = obj.intersection_with(raio)
        # falta verificar se t é vazio
        print(obj, obj.ponto(t))
