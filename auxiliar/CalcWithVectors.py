import numpy as np


def produto_escalar(vetor1: object, vetor2: object) -> object:
    return np.sqrt(np.dot(vetor1, vetor2))


def produto_vetorial(vetor1, vetor2):
    return np.cross(vetor1, vetor2)
