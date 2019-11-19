import numpy as np

from DataStructure.Edge import Edge
from DataStructure.Face import Face
from DataStructure.Point import Point
from utils.Ray import Ray


def calc_vertices(centro, aresta):
    vertices = []
    v0 = Point(centro.x + (aresta / 2), centro.y, centro.z + (aresta / 2), "0")
    v1 = Point(centro.x + (aresta / 2), centro.y, centro.z - (aresta / 2), "1")
    v2 = Point(centro.x - (aresta / 2), centro.y, centro.z - (aresta / 2), "2")
    v3 = Point(centro.x - (aresta / 2), centro.y, centro.z + (aresta / 2), "3")
    v4 = Point(centro.x + (aresta / 2), centro.y + aresta, centro.z + (aresta / 2), "4")
    v5 = Point(centro.x + (aresta / 2), centro.y + aresta, centro.z - (aresta / 2), "5")
    v6 = Point(centro.x - (aresta / 2), centro.y + aresta, centro.z - (aresta / 2), "6")
    v7 = Point(centro.x - (aresta / 2), centro.y + aresta, centro.z + (aresta / 2), "7")

    vertices.append(v0)
    vertices.append(v1)
    vertices.append(v2)
    vertices.append(v3)
    vertices.append(v4)
    vertices.append(v5)
    vertices.append(v6)
    vertices.append(v7)
    return vertices


def calc_arestas(l_v):
    arestas = [Edge(l_v[0], l_v[1]), Edge(l_v[1], l_v[2]), Edge(l_v[2], l_v[3]), Edge(l_v[3], l_v[0]),
               Edge(l_v[0], l_v[4]), Edge(l_v[1], l_v[5]), Edge(l_v[2], l_v[6]), Edge(l_v[3], l_v[7]),
               Edge(l_v[4], l_v[5]), Edge(l_v[5], l_v[6]), Edge(l_v[6], l_v[7]), Edge(l_v[7], l_v[4])]
    return arestas


def calc_faces(l_v):
    faces = [Face(l_v[1], l_v[0], l_v[3]), Face(l_v[1], l_v[3], l_v[2]), Face(l_v[4], l_v[0], l_v[1]),
             Face(l_v[4], l_v[1], l_v[5]), Face(l_v[5], l_v[1], l_v[2]), Face(l_v[5], l_v[2], l_v[6]),
             Face(l_v[6], l_v[2], l_v[3]), Face(l_v[6], l_v[3], l_v[7]), Face(l_v[7], l_v[3], l_v[0]),
             Face(l_v[7], l_v[0], l_v[4]), Face(l_v[5], l_v[6], l_v[7]), Face(l_v[5], l_v[7], l_v[4])]
    return faces


class Cube:
    def __init__(self, centro, vetor, aresta, material=None, cor=None):
        self.__centro = centro
        self.__n = vetor / np.linalg.norm(vetor)
        self.__aresta = aresta
        self.__lista_vertices = calc_vertices(centro, aresta)
        self.__lista_arestas = calc_arestas(self.lista_vertices)
        self.__lista_faces = calc_faces(self.lista_vertices)
        self.__material = material
        self.__cor = cor

    def intersection_with(self, reta: Ray):
        t_min = 99999999
        for face in self.lista_faces:
            if np.dot(reta.d, face.normal_vector) != 0:
                t = np.dot(face.p1.coord - reta.p.coord, face.normal_vector) \
                    / np.dot(reta.d, face.normal_vector)
                p = reta.get_point(t)

                pv1 = np.cross(face.p2.coord - face.p1.coord, face.p1.coord - p.coord)
                pv2 = np.cross(face.p3.coord - face.p2.coord, face.p2.coord - p.coord)
                pv3 = np.cross(face.p1.coord - face.p3.coord, face.p3.coord - p.coord)
                pv0 = np.cross(face.p2.coord - face.p1.coord, face.p3.coord - face.p1.coord)

                if np.dot(pv1, pv0) > 0:
                    if np.dot(pv2, pv0) > 0:
                        if np.dot(pv3, pv0) > 0:
                            if t < t_min:
                                t_min = t
        return t_min

    def transforme_coord_to_(self, c):
        pass

    @property
    def centro(self):
        return self.__centro

    @property
    def n(self):
        return self.__n

    @property
    def aresta(self):
        return self.__aresta

    @property
    def lista_vertices(self):
        return self.__lista_vertices

    @property
    def lista_aresta(self):
        return self.__lista_arestas

    @property
    def lista_faces(self):
        return self.__lista_faces

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, m):
        self.__material = m
