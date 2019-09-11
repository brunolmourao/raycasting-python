from typing import List, Union

from geometricAttributes.Point import Point
from utils.constant import POSICAO_PLACA_Z


class Panel:
    __p = []

    def __init__(self, tam, num_lin, num_col):
        """O centro do painel tem coordenada [0,0,z]
               deste modo os vertices tem coord:
               [-tam/2, tam/2, z]  ______ [tam/2,  tam/2, z]
                                  |  .  |
               [-tam/2,-tam/2, z] |_____| [tam/2, -tam/2, z]
           """
        if tam / num_lin >= tam / num_col:
            var = tam / num_col
        else:
            var = tam / num_lin

        for lin in range(num_lin):
            p_linha: List[List[Union[Point, str]]] = []
            for col in range(num_col):
                x_lc = -tam / 2 + var * (1 + 2 * col) / 2
                y_lc = tam / 2 - var * (1 + 2 * lin) / 2
                p_linha.append([Point(x_lc, y_lc, POSICAO_PLACA_Z), '.'])
            self.__p.append(p_linha)

    @property
    def p(self):
        return self.__p

    def set_simbolo_furo(self, l, c, valor):
        self.__p[l][c][1] = valor

    def show(self):
        for lin in range(len(self.__p)):
            for col in range(len(self.__p[lin])):
                # print(" [", lin, col, "]", self.__p[lin][col][1], end="")
                print(self.p[lin][col][1], end="")
            print()
