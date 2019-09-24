from typing import List, Union
import numpy as np
from geometricAttributes.Point import Point
from utils import constant
from utils.Transform import transform_to_camera
from utils.constant import POSICAO_PLACA_Z
from light.Lighting import EnvironmentLight


class Panel:
    __p = []

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
            p_linha: List[Point] = []
            for col in range(num_col):
                x_lc = -tam / 2 + var * (1 + 2 * col) / 2
                y_lc = tam / 2 - var * (1 + 2 * lin) / 2
                p_linha.append(Point(x_lc, y_lc, constant.POSICAO_PLACA_Z))
            p.append(p_linha)
        self.__p = p

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

    def transform_to_camera(self, camera):
        # TODO testar
        for p in self.p:
            p = transform_to_camera(camera, p)


class Tela:
    __p = []

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
                p_linha.append([Point(x_lc, y_lc, POSICAO_PLACA_Z), '.'])
                p.append(p_linha)
        self.__p = p

    def transform_to_camera(self, camera):
        # TODO testar
        for p in self.__p:
            p[0] = transform_to_camera(camera, p[0])

    def show(self):
        for lin in range(len(self.__p)):
            for col in range(len(self.__p[lin])):
                # print(" [", lin, col, "]", self.__p[lin][col][1], end="")
                print(self.p[lin][col][1], end="")
            print()

    @property
    def p(self):
        return self.__p

    def set_simbolo_furo(self, l, c, valor):
        self.__p[l][c][1] = valor

    def set_cor(self, l, c, material, t, f_luz):
        cor = np.array([])
        # TODO Calcular a iluminação no ponto t
        # cor = f_luz[0].iluminar(material.ka())
        for f in f_luz:
            if isinstance(f, EnvironmentLight):
                cor = f_luz[0].iluminar(material.ka())
            else:
                cor = cor + f.iluminar_dif(material.kd()) + f.iluminar_sp(material.ks())
        self.__p[l][c][1] = cor
