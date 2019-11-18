from DataStructure.Face import Face
from DataStructure.Point import Point
from DataStructure.Vector import Vector
from Object.Cone import Cone
from Object.Cube import Cube
from Object.Cylinder import Cylinder
from Object.Plane import Plane
from Object.Sphere import Sphere
from utils.Ray import Ray

a = Point(0, 1, 2)
b = Point(1, 3, 2)
c = Point(5, 2, 8)

v1 = Vector(a, b)
v2 = Vector(b, c)
v3 = Vector(c, a)

f1 = Face(a, b, c)
v = Vector(Point(0, 0, 0), a)
r = Ray(c, v.coord)

plano = Plane(b, v1.coord)
esfera = Sphere(b, 10)
cilindro = Cylinder(a, v1.coord, 10, 30)
cone = Cone(a, v1.coord, 10, 30)

print(a.coord, b.coord, c.coord)
print(v1.coord, v2.coord, v3.coord)
# print(f1.normal_vector)

# print("v: ", v)
# print(v1.coord)# https://www.wolframalpha.com/input/?i=plane+through+point+%281%2C3%2C2%29+with+normal+vector+%281%2Fsqrt+5%2C+2%2F+sqrt+5%2C0%29
# print(v.coord) # https://www.wolframalpha.com/input/?i=line+through+%285%2C2%2C8%29+and+vector+%280%2C1%2Fsqrt5%2C2%2Fsqrt5%29
# print(plano.n)
# print(r.d)

# print(plano.intersection_with(r))
# print(r.get_point(plano.intersection_with(r)).coord)

# print(esfera.intersection_with(r)) # https://www.wolframalpha.com/input/?i=sphere+center+%281%2C3%2C2%29+radius10
# print(r.get_point(esfera.intersection_with(r)).coord) #https://www.wolframalpha.com/input/?i=x%3D5%2C+z%3D2k%2B8%2Cy%3Dk%2B2%2C+%28y-3%29%5E2%2B%28z-2%29%5E2+%3D+84

print("========")

# print(cilindro.intersection_with(r)) # https://www.wolframalpha.com/input/?i=cylinder+center+%285%2C2%2C8%29+radius10%2C+height30+with+normal+vector+%281%2Fsqrt+5%2C+2%2F+sqrt+5%2C0%29
# print("final: ", r.get_point(cilindro.intersection_with(r)).coord)

# print("final: ", r.get_point(cone.intersection_with(r)).coord)

cubo = Cube(a, Point(0, 1, 0).coord, 10)
for i in cubo.lista_vertices:
    print(i.label, " - ", i.coord)
for i in cubo.lista_aresta:
    print(i.label, " - ", i.s.label, "\t", i.d.label)
for i in cubo.lista_faces:
    print(i.label, " - ", i.normal_vector)

print("cubo final", r.get_point(cubo.intersection_with(r)).coord)
