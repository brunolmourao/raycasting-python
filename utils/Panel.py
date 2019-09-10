from typing import List, Union

from geometricAttributes.Point import Point


class Panel:
    __p = []
    __pos = 0

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
                p_linha.append([Point(x_lc, y_lc, self.pos), '.', Point(0, 0, 0)])
            self.__p.append(p_linha)

    def print(self):
        pass

    @property
    def p(self):
        return self.__p

    def set_simbolo_furo(self, l, c, valor):
        self.__p[l][c][1] = valor

    def set_t_furo(self, l, c, valor):
        self.__p[l][c][2]

    def show(self):
        for lin in range(len(self.__p)):
            for col in range(len(self.__p[lin])):
                # print(" [", lin, col, "]", self.__p[lin][col][1], end="")
                print(self.p[lin][col][1], end="")
            print()

    def pos(self):
        return self.__pos

    def pos(self, a):
        self.__pos = a
