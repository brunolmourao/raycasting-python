import numpy as np

from geometricAttributes.Face import Face
from geometricAttributes.Point import Point
from utils.Transform import transform_to_camera


def validar_tint(p, p1, p2, p3):
    p1p = p1 - p
    p2p = p2 - p
    p3p = p3 - p
    v1v2 = np.cross(p1p, p2p)
    v2v3 = np.cross(p2p, p3p)
    v3v1 = np.cross(p3p, p1p)
    if np.dot(v1v2, v2v3) > 0:
        if np.dot(v1v2, v3v1) > 0:
            return True
    return False


# Calcula a normal a face triangular
def calc_normal(f1, f2, f3):
    v1 = f2 - f1
    v2 = f3 - f1
    N = np.cross(v1, v2)
    n = N / np.linalg.norm(N)
    return n


class Cube(object):

    def __init__(self, centro_base, aresta, v_direcao,material):
        self.__lista_vertices = self.calc_verticies(centro_base, aresta)
        self.__lista_arestas = self.calc_arestas()
        self.__lista_faces = self.calc_faces()
        self.v_direcao = v_direcao
        self.cor = ""
        self.material = material

    def intersection_with(self, reta):
        t = []
        for face in self.__lista_faces:
            f1 = face.p1.coords()
            f2 = face.p2.coords()
            f3 = face.p3.coords()
            n = calc_normal(f1, f2, f3)
            p0 = reta.p.coords()
            d = reta.v_direcao
            if np.dot(d, n) != 0:
                tint = np.dot(f1 - p0, n) / np.dot(d, n)
                p = reta.ponto(tint)
                if validar_tint(p.coords(), f1, f2, f3):
                    t.append(tint)
        return t

    @staticmethod
    def calc_verticies(centro_base, aresta):
        vertices = []
        v1 = Point(centro_base.x + (aresta / 2), centro_base.y, centro_base.z + (aresta / 2))
        v2 = Point(centro_base.x + (aresta / 2), centro_base.y, centro_base.z - (aresta / 2))
        v3 = Point(centro_base.x - (aresta / 2), centro_base.y, centro_base.z - (aresta / 2))
        v4 = Point(centro_base.x - (aresta / 2), centro_base.y, centro_base.z + (aresta / 2))
        v5 = Point(centro_base.x + (aresta / 2), centro_base.y + aresta, centro_base.z + (aresta / 2))
        v6 = Point(centro_base.x + (aresta / 2), centro_base.y + aresta, centro_base.z - (aresta / 2))
        v7 = Point(centro_base.x - (aresta / 2), centro_base.y + aresta, centro_base.z - (aresta / 2))
        v8 = Point(centro_base.x - (aresta / 2), centro_base.y + aresta, centro_base.z + (aresta / 2))

        vertices.append(["0", v1])  # lista com íd e o vérticie correspondente
        vertices.append(["1", v2])
        vertices.append(["2", v3])
        vertices.append(["3", v4])
        vertices.append(["4", v5])
        vertices.append(["5", v6])
        vertices.append(["6", v7])
        vertices.append(["7", v8])
        return vertices

    # Calcular Arestas a partir dos vérticies
    def calc_arestas(self):
        #TODO A LISTA DE ARESTA ESTA ERRADO O CORRETO SERIA
        "01-12-23-30 | 04-15-26-37 | 45-56-67-74"
        arestas = []
        lista_v = self.__lista_vertices
        # Arestas da Base
        arestas.append(["01", lista_v[0][1], lista_v[1][1]])  # lista com id, vértice 1 e verticie 2
        arestas.append(["12", lista_v[1][1], lista_v[2][1]])
        arestas.append(["23", lista_v[2][1], lista_v[3][1]])
        arestas.append(["30", lista_v[3][1], lista_v[0][1]])
        # Arestas entre as bases
        arestas.append(["04", lista_v[0][1], lista_v[4][1]])
        arestas.append(["15", lista_v[1][1], lista_v[5][1]])
        arestas.append(["26", lista_v[2][1], lista_v[6][1]])
        arestas.append(["37", lista_v[3][1], lista_v[7][1]])
        # Arestas da Base Superior
        arestas.append(["45", lista_v[4][1], lista_v[5][1]])
        arestas.append(["56", lista_v[5][1], lista_v[6][1]])
        arestas.append(["67", lista_v[6][1], lista_v[7][1]])
        arestas.append(["74", lista_v[7][1], lista_v[4][1]])

        print(arestas[0])
        return arestas

        """
        # Arestas da Base
        arestas.append([1, lista_v[0][1], lista_v[2][1]])  # lista com id, vértice 1 e verticie 2
        arestas.append([2, lista_v[0][1], lista_v[3][1]])
        arestas.append([3, lista_v[3][1], lista_v[1][1]])
        arestas.append([4, lista_v[1][1], lista_v[2][1]])
        # Arestas entre as bases
        arestas.append([5, lista_v[0][1], lista_v[4][1]])
        arestas.append([6, lista_v[3][1], lista_v[7][1]])
        arestas.append([7, lista_v[1][1], lista_v[5][1]])
        arestas.append([8, lista_v[2][1], lista_v[6][1]])
        # Arestas da Base Superior
        arestas.append([9, lista_v[4][1], lista_v[6][1]])
        arestas.append([10, lista_v[4][1], lista_v[7][1]])
        arestas.append([11, lista_v[7][1], lista_v[5][1]])
        arestas.append([12, lista_v[5][1], lista_v[6][1]])
        """

        return arestas

    # Calcular Faces Triangulares a partir dos Vérticies
    def calc_faces(self):
        #TODO acho que as faces estao com o vetor normal pra dentro
        faces = []
        lista_v = self.__lista_vertices
        # Faces Triangulares da Base
        faces.append(Face("032", lista_v[0][1], lista_v[3][1], lista_v[2][1]))
        faces.append(Face("021", lista_v[0][1], lista_v[2][1], lista_v[1][1]))
        # Faces Triangulares das faces laterais
        faces.append(Face("140", lista_v[1][1], lista_v[4][1], lista_v[0][1]))
        faces.append(Face("154", lista_v[1][1], lista_v[5][1], lista_v[4][1]))

        faces.append(Face("251", lista_v[2][1], lista_v[5][1], lista_v[1][1]))
        faces.append(Face("265", lista_v[2][1], lista_v[6][1], lista_v[5][1]))

        faces.append(Face("362", lista_v[3][1], lista_v[6][1], lista_v[2][1]))
        faces.append(Face("376", lista_v[3][1], lista_v[7][1], lista_v[6][1]))

        faces.append(Face("047", lista_v[0][1], lista_v[4][1], lista_v[7][1]))
        faces.append(Face("073", lista_v[0][1], lista_v[7][1], lista_v[3][1]))
        # Faces Triangulares da Base Superior
        faces.append(Face("456", lista_v[4][1], lista_v[5][1], lista_v[6][1]))
        faces.append(Face("467", lista_v[4][1], lista_v[6][1], lista_v[7][1]))

        return faces

    def set_cor(self, cor):
        self.cor = cor

    def transform_to_camera(self, camera):
        # TODO testar
        for v in self.__lista_vertices:
            ponto = np.append(v, [1])
            produto = np.dot(camera, ponto)
            v[1] = Point(produto.item(0), produto.item(1), produto.item(2))
        self.__lista_arestas = self.calc_arestas()
        self.__lista_faces = self.calc_faces()
