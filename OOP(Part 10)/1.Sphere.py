import math


class Sphere(object):
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x, y, z):
        self.center = (x, y, z)


sphere = Sphere(5, 3, 2, 1)
print('Объем шара =', sphere.get_volume())
print('Площадь внешней поверхности схемы =', sphere.get_square())
print('Радиус = ', sphere.get_radius(), '; Центр =', sphere.get_center())
sphere.set_radius(200)
sphere.set_center(10, 22, 33)
print('Радиус = ', sphere.get_radius(), '; Центр', sphere.get_center())
