"""A classe Cube define um CUBO.
    Atributos
    centro_base: Ponto
        Um ponto com as coordenadas do centro da base
    aresta: float
        O tamanho da aresta do cubo
    v_direcao: Vetor
        Um vetor unitario que é a normal a base do cubo
"""


class Cube(object):
    __lista_vertices = []
    __lista_arestas = []
    __lista_faces = []

    # TODO: criar construtor. A partir dos dados de entrada,
    # criar as listas de 8 vertices (id, p_ori, p_dest), 16 arestas(id,v_orig, v_dest),
    # e 12 faces triangulares (id, vert1, vert2, vert3)
    def __init__(self, centro_base, aresta, v_direcao):
        pass

    # TODO: implementar a equação de interseção com a reta
    # Pecorrer a lista de faces triangulares e usar o meto
    @staticmethod
    def intersection_with(self, reta):
        """retona uma lista de t's dos pontos"""
        t = []

        return t
