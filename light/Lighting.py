import numpy as np
import utils.CalcWithVectors as calc


class Light:
    # Inicia a Luz com um Atributo rgb que é um array com os valores RGB, entre 0 e 1
    def __init__(self, rgb):
        self.__rgb = rgb

    # Calcula o vetor resultante da interação da Luz com o material do objeto
    def arroba(self, prop_obj):
        result = []
        for x in range(3):
            result.append(self.__rgb[x] * prop_obj[x])
        return result


# Luz Ambiente herda os atributos de Light
class EnvironmentLight(Light):
    def __init__(self, rgb):
        super().__init__(rgb)

    def iluminar(self, prop_obj):
        return super().arroba(prop_obj)


class PointLight(Light):
    # Onde ppnt é o Ponto de onde a luz pontual é gerada
    def __init__(self, rgb, ppont):
        super().__init__(rgb)
        self.__ppont = ppont

    def iluminar_dif(self, prop_obj, n, pint):
        l = self.__ppont - pint / np.linalg.norm(self.__ppont - pint)
        fd = calc.produto_escalar(n, l)
        if fd < 0:
            fd = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fd
        return product

    def iluminar_sp(self, prop_obj, n, p0, pint, m):
        l = self.__ppont - pint / np.linalg.norm(self.__ppont - pint)
        v = p0 - pint / calc.norma(p0 - pint)
        r = 2 * np.dot(l, n) * n - l
        fs = np.power(np.dot(r, v), m)
        if fs < 0:
            fs = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fs
        return product


class SpotLight(Light):
    def __init__(self, rgb, pspot, pilu):
        super().__init__(rgb)
        self.__pspot = pspot
        self.__dr = pilu - pspot

    def iluminar_dif(self, prop_obj, n):
        l = self.__dr
        fd = calc.produto_escalar(n, l)
        if fd < 0:
            fd = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fd
        return product

    def iluminar_sp(self, prop_obj, n, p0, pint, m):
        l = self.__dr
        v = p0 - pint / calc.norma(p0 - pint)
        r = 2 * np.dot(l, n) * n - l
        fs = np.power(np.dot(r, v), m)
        if fs < 0:
            fs = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fs
        return product


class RemoteLight(Light):
    def __init__(self, rgb, dr):
        super().__init__(rgb)
        self.__dr = dr

    def iluminar_dif(self, prop_obj, n):
        l = self.__dr
        fd = calc.produto_escalar(n, l)
        if fd < 0:
            fd = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fd
        return product

    def iluminar_sp(self, prop_obj, n, p0, pint, m):
        l = self.__dr
        v = p0 - pint / calc.norma(p0 - pint)
        r = 2 * np.dot(l, n) * n - l
        fs = np.power(np.dot(r, v), m)
        if fs < 0:
            fs = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fs
        return product


"""
luz1 = EnvironmentLight([0.5, 0.5, 1])
luz2 = PointLight([0.5, 0.5, 1], np.array([1, 1, 1]))
luz3 = SpotLight([0.5, 0.4, 0.8], np.array([2, 2, 0]), np.array([1, 1, 0]))
luz4 = RemoteLight([0.5, 0.5, 0.8], np.array([0, 1, 0]))

p_dif = [1, 1, 1]
p_sp = [0, 0.5, 0.4]
n = np.array([0, 1, 0])
print(luz1.iluminar(p_dif))
print(luz1.iluminar(p_sp))
print(luz2.iluminar_dif(p_dif, n, np.array([2, 2, 2])))
"""
