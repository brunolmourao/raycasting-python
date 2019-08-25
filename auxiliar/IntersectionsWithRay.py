from auxiliar import QuadraticOperations

""" !!!! ATENÇÃO" !!!! Minha sugestão @Alysson
    as tarefas que competem a esta classe vão ser dristribuídas pra cada objeto.
     Cada Objeto calculará os pontos de interseçção de si mesmmo com a reta. 
"""


class IntersectionsWithRay:

    @staticmethod
    def with_plane(self, plane, ray):
        return ((plane.ppl - ray.p0) * plane.vet_n) / (ray.vet_n * plane.vet_n)
        """esta errado, é preciso usar NUMPY para
        calculo com vetores. Veja esse link http://www.robertocolistete.net/ICF/ipynb/Vetores-Python/Vetores-Python.pdf
        
        O produto via "*" não é produto escalar, e sim o produto de termo a termo de cada vetor :
        [1,2,3]*[6,2,5] = [6,4,15]
              
        """

    @staticmethod
    def with_sphere(self, sphere, ray):
        a = ray.vet_n * ray.vet_n
        b = (ray.p0 - sphere.c) * ray.vet_n
        c = (ray.p0 - sphere.c) * (ray.p0 - sphere.c) - sphere.r * sphere.r
        return QuadraticOperations.roots(a, b, c)
