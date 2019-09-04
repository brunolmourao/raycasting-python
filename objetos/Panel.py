from typing import List, Union

from estruturaDeDados.Point import Point


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
        p = []
        if tam / num_lin >= tam / num_col:
            var = tam / num_col
        else:
            var = tam / num_lin

        for lin in range(num_lin):
            p_linha: List[List[Union[Point, str]]] = []
            for col in range(num_col):
                x_lc = -tam / 2 + var * (1 + 2 * col) / 2
                y_lc = tam / 2 - var * (1 + 2 * lin) / 2
                p_linha.append([Point(x_lc, y_lc, self.pos), '.'])
            p.append(p_linha)

    def print(self):
        pass

    @property
    def p(self):
        return self.p

    def pos(self):
        return self.__pos

    def pos(self, a):
        self.__pos = a
