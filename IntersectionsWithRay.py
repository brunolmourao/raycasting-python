import QuadraticOperations


class IntersectionsWithRay:

    @staticmethod
    def with_plane(self, plane, ray):
        return ((plane.ppl - ray.p0) * plane.vet_n) / (ray.vet_n * plane.vet_n)

    @staticmethod
    def with_sphere(self, sphere, ray):
        a = ray.vet_n * ray.vet_n
        b = (ray.p0 - sphere.c) * ray.vet_n
        c = (ray.p0 - sphere.c) * (ray.p0 - sphere.c) - sphere.r * sphere.r
        return QuadraticOperations.roots(a, b, c)

