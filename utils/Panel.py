from DataStructure.Point import Point
from utils.constants import Z_PLACA
import numpy as np

class Panel:
    def __init__(self, tam, n_linhas, n_colunas):
        self.__tam = tam
        self.__num_l = n_linhas
        self.__num_c = n_colunas
        self.__matrix_pixel = np.full((n_linhas, n_colunas), ".")

    def get_p(self, i, j):
        if self.tam / self.n_lin >= self.tam / self.n_col:
            var = self.tam / self.n_col
        else:
            var = self.tam / self.n_lin
        x = -self.tam / 2 + var * (1 + 2 * j) / 2
        y = self.tam / 2 - var * (1 + 2 * i) / 2
        z = Z_PLACA
        return Point(x, y, z)

    def set_cor(self, l, c, v):
        self.matrix_pixel[l][c] = v

    def transforme_coord_to_(self, c, p):
        pass

    def show(self):
        i = 0
        for l in range(len(self.matrix_pixel)):
            for c in range(len(self.matrix_pixel[l])):
                print(f"{self.matrix_pixel[l][c]}", end=" ")
                i = i + 1
            print()

    @property
    def tam(self):
        return self.__tam

    @property
    def n_lin(self):
        return self.__num_l

    @property
    def n_col(self):
        return self.__num_c

    @property
    def matrix_pixel(self):
        return self.__matrix_pixel
