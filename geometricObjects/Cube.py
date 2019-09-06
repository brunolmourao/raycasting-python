"""A classe Cube define um CUBO.
    Atributos
    centro_base: Ponto
        Um ponto com as coordenadas do centro da base
    aresta: float
        O tamanho da aresta do cubo
    v_direcao: Vetor
        Um vetor unitario que é a normal a base do cubo
"""

from geometricAttributes.Point import Point
from utils.Ray import Ray


class Cube(object):
    __lista_vertices = []
    __lista_arestas = []
    __lista_faces = []

    # Método construtor do cubo , alocando todas as listas necessárias
    def __init__(self, centro_base, aresta, v_direcao):
        self.calc_verticies(centro_base, aresta)
        self.calc_arestas()
        self.calc_faces()
        self.v_direcao = v_direcao

    # TODO: implementar a equação de interseção com a reta
    # Pecorrer a lista de faces triangulares e usar o meto
    
    def intersection_with(self, reta):
        """retona uma lista de t's dos pontos"""
        t = []

        return t

    # Calcular os vértices a partir das entradas e colocar na lista
    def calc_verticies(self, centro_base, aresta):
        base_top_y = centro_base.y + aresta
        base_top = Point(centro_base.x, base_top_y, centro_base.z)  # ponto central da base superior
        # base_top.print_ponto()
        v1 = Point(centro_base.x + (aresta / 2), centro_base.y, centro_base.z + (aresta / 2))
        v2 = Point(centro_base.x - (aresta / 2), centro_base.y, centro_base.z - (aresta / 2))
        v3 = Point(centro_base.x + (aresta / 2), centro_base.y, centro_base.z - (aresta / 2))
        v4 = Point(centro_base.x - (aresta / 2), centro_base.y, centro_base.z + (aresta / 2))
        v5 = Point(base_top.x + (aresta / 2), base_top.y, base_top.z + (aresta / 2))
        v6 = Point(base_top.x - (aresta / 2), base_top.y, base_top.z - (aresta / 2))
        v7 = Point(base_top.x + (aresta / 2), base_top.y, base_top.z - (aresta / 2))
        v8 = Point(base_top.x - (aresta / 2), base_top.y, base_top.z + (aresta / 2))
        self.__lista_vertices.append([0, v1])  # lista com íd e o vérticie correspondente
        self.__lista_vertices.append([1, v2])
        self.__lista_vertices.append([2, v3])
        self.__lista_vertices.append([3, v4])
        self.__lista_vertices.append([4, v5])
        self.__lista_vertices.append([5, v6])
        self.__lista_vertices.append([6, v7])
        self.__lista_vertices.append([7, v8])

    # Calcular Arestas a partir dos vérticies
    def calc_arestas(self):
        lista_v = self.__lista_vertices
        # Arestas da Base
        self.__lista_arestas.append([1, lista_v[0][1], lista_v[2][1]])  # lista com id, vértice 1 e verticie 2
        self.__lista_arestas.append([2, lista_v[0][1], lista_v[3][1]])
        self.__lista_arestas.append([3, lista_v[3][1], lista_v[1][1]])
        self.__lista_arestas.append([4, lista_v[1][1], lista_v[2][1]])
        # Arestas entre as bases
        self.__lista_arestas.append([5, lista_v[0][1], lista_v[4][1]])
        self.__lista_arestas.append([6, lista_v[3][1], lista_v[7][1]])
        self.__lista_arestas.append([7, lista_v[1][1], lista_v[5][1]])
        self.__lista_arestas.append([8, lista_v[2][1], lista_v[6][1]])
        # Arestas da Base Superior
        self.__lista_arestas.append([9, lista_v[4][1], lista_v[6][1]])
        self.__lista_arestas.append([10, lista_v[4][1], lista_v[7][1]])
        self.__lista_arestas.append([11, lista_v[7][1], lista_v[5][1]])
        self.__lista_arestas.append([12, lista_v[5][1], lista_v[6][1]])

    # Calcular Faces Triangulares a partir dos Veérticies
    def calc_faces(self):
        lista_v = self.__lista_vertices
        # Faces Triangulares da Base
        self.__lista_faces.append([1, lista_v[0][1], lista_v[1][1], lista_v[3][1]])
        self.__lista_faces.append([2, lista_v[0][1], lista_v[1][1], lista_v[2][1]])
        # Faces Triangulares das faces laterais
        self.__lista_faces.append([3, lista_v[0][1], lista_v[3][1], lista_v[7][1]])
        self.__lista_faces.append([4, lista_v[0][1], lista_v[4][1], lista_v[7][1]])
        self.__lista_faces.append([5, lista_v[0][1], lista_v[2][1], lista_v[4][1]])
        self.__lista_faces.append([6, lista_v[6][1], lista_v[2][1], lista_v[4][1]])
        self.__lista_faces.append([7, lista_v[1][1], lista_v[2][1], lista_v[5][1]])
        self.__lista_faces.append([8, lista_v[2][1], lista_v[5][1], lista_v[6][1]])
        self.__lista_faces.append([9, lista_v[1][1], lista_v[3][1], lista_v[7][1]])
        self.__lista_faces.append([10, lista_v[1][1], lista_v[4][1], lista_v[7][1]])
        # Faces Triangulares da Base Superior
        self.__lista_faces.append([11, lista_v[4][1], lista_v[5][1], lista_v[7][1]])
        self.__lista_faces.append([12, lista_v[4][1], lista_v[5][1], lista_v[6][1]])
