class Cylinder:
    def __init__(self, heights=1, radius=1):
        self.heights = heights
        self.rad = radius

        pass

    def volume(self):
        print(3.14 * (self.rad**2) * self.heights)

    def surface_area(self):

        pi = 3.14

        print((2*pi) * (self.heights * self.rad) + (2*pi) * (self.rad**2))


c = Cylinder(2, 3)
c.volume()

c.surface_area()
