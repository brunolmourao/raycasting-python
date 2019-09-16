import numpy as np


class Translation:
    # Translada o ponto de um lugar para outro
    def __init__(self, t):
        self.__t = t

    # Calcula o ponto resultante da translação
    def transladar(self, point):
        result = []
        for i in range(3):
            result.append(self.__t[i] + point[i])
        return result


class Scale:
    # Aplica a matriz de Escala a um determinado ponto
    def __init__(self, s):
        self.__s = s

    # Calcula o novo ponto ao ser aplicada a matriz de Escala
    def escala(self, point):
        result = []
        for i in range(3):
            result.append(self.__s[i] * point[i])
        return result


class Rotation:
    # Aplica a rotação de um ponto em um determinado ângulo theta
    def __init__(self, theta):
        self.__sin_theta = np.sin(np.deg2rad(theta))
        self.__cos_theta = np.cos(np.deg2rad(theta))

    # Calcula o ponto após a rotação em torno do eixo x
    def rotacionar_x(self, point):
        result = []

        x = point[0]
        y = point[1] * self.__cos_theta - point[2] * self.__sin_theta
        z = point[1] * self.__sin_theta + point[2] * self.__cos_theta

        result.append(x)
        result.append(y)
        result.append(z)

        return result

    # Calcula o ponto após a rotação em torno do eixo y
    def rotacionar_y(self, point):
        result = []

        x = point[0] * self.__cos_theta + point[2] * self.__sin_theta
        y = point[1]
        z = point[2] * self.__cos_theta - point[0] * self.__sin_theta

        result.append(x)
        result.append(y)
        result.append(z)

        return result

    # Calcula o ponto após a rotação em torno do eixo z
    def rotacionar_z(self, point):
        result = []

        x = point[0] * self.__cos_theta - point[1] * self.__sin_theta
        y = point[0] * self.__sin_theta + point[1] * self.__cos_theta
        z = point[2]

        result.append(x)
        result.append(y)
        result.append(z)

        return result


class Mirroring:

    # Calcula o novo ponto em relação ao espelho xz
    def espelhar_xz(self, point):
        result = []

        result.append(point[0])
        result.append((-1) * point[1])
        result.append(point[2])

        return result

    # Calcula o novo ponto em relação ao espelho yz
    def espelhar_yz(self, point):
        result = []

        result.append((-1) * point[0])
        result.append(point[1])
        result.append(point[2])

        return result

    # Calcula o novo ponto em relação ao espelho xy
    def espelhar_xy(self, point):
        result = []

        result.append(point[0])
        result.append(point[1])
        result.append((-1) * point[2])

        return result

