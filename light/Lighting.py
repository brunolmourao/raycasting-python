import numpy as np

from DataStructure.Point import Point


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
    def __init__(self, rgb, ppont: Point):
        super().__init__(rgb)
        self.__ppont = ppont

    def iluminar_dif(self, prop_obj, n, pint: Point):
        l = self.__ppont.coord - pint.coord / np.linalg.norm(self.__ppont.coord - pint.coord)
        fd = np.dot(n, l)
        if fd < 0:
            fd = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fd
        return product

    def iluminar_sp(self, prop_obj, n, p0: Point, pint: Point, m):
        l = self.__ppont.coord - pint.coord / np.linalg.norm(self.__ppont.coord - pint.coord)
        v = p0.coord - pint.coord / np.linalg.norm(p0.coord - pint.coord)
        r = 2 * np.dot(l, n) * n - l
        fs = np.power(np.dot(r, v), m)
        if fs < 0:
            fs = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fs
        return product

    def transforme_coord_to_(self, c):
        p_2D = np.append(self.__ppont.coord, 0)[:, np.newaxis]
        new_p_2D = np.dot(c, p_2D)
        new_p_1D = new_p_2D.transpose().squeeze()
        new_p = np.delete(new_p_1D, 3, 0)
        self.__ppont = Point(new_p[0], new_p[1], new_p[2])


class SpotLight(Light):
    #TODO Esse pilu deveria ser um vetor. Correto?
    def __init__(self, rgb, pspot: Point, pilu: Point):
        super().__init__(rgb)
        self.__p = pspot
        self.__dr = pilu.coord - pspot.coord

    def iluminar_dif(self, prop_obj, n):
        l = self.__dr
        fd = np.dot(n, l)
        if fd < 0:
            fd = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fd
        return product

    def iluminar_sp(self, prop_obj, n, p0: Point, pint: Point, m):
        l = self.__dr
        v = p0.coord - pint.coord / np.linalg.norm(p0.coord - pint.coord)
        r = 2 * np.dot(l, n) * n - l
        fs = np.power(np.dot(r, v), m)
        if fs < 0:
            fs = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fs
        return product

    def transforme_coord_to_(self, c):
        p_2D = np.append(self.__p.coord, 0)[:, np.newaxis]
        new_p_2D = np.dot(c, p_2D)
        new_p_1D = new_p_2D.transpose().squeeze()
        new_p = np.delete(new_p_1D, 3, 0)
        self.__p = Point(new_p[0], new_p[1], new_p[2])

        dr_2D = np.append(self.__dr, 1)[:, np.newaxis] #TODO tem um erro aqui, 'self.__dr' está sendo visto como um Point, quando deveria ser um vetor (np.array)
        new_dr_2D = np.dot(c, dr_2D)
        new_dr_1D = new_dr_2D.transpose().squeeze()
        new_dr = np.delete(new_dr_1D, 3, 0)
        self.__dr = Point(new_dr[0], new_dr[1], new_dr[2])


class RemoteLight(Light):
    def __init__(self, rgb, dr):
        super().__init__(rgb)
        self.__dr = dr

    def iluminar_dif(self, prop_obj, n):
        l = self.__dr
        fd = np.dot(n, l)
        if fd < 0:
            fd = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fd
        return product

    def iluminar_sp(self, prop_obj, n, p0: Point, pint: Point, m):
        l = self.__dr
        v = p0.coord - pint.coord / np.linalg.norm(p0.coord - pint.coord)
        r = 2 * np.dot(l, n) * n - l
        fs = np.power(np.dot(r, v), m)
        if fs < 0:
            fs = 0
        product = super().arroba(prop_obj)
        for x in range(3):
            product[x] = product[x] * fs
        return product

    def transforme_coord_to_(self, c):
        p_2D = np.append(self.__dr.coord, 1)[:, np.newaxis]
        new_p_2D = np.dot(c, p_2D)
        new_p_1D = new_p_2D.transpose().squeeze()
        new_p = np.delete(new_p_1D, 3, 0)
        self.__dr = Point(new_p[0], new_p[1], new_p[2])
