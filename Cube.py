from p5 import *
class Cube:
    def __init__(self, x, y, z, scale):
        self.position = Vector(x, y, z)
        self.scale = scale

    def generate(self):
        cubes = []
        verticies = [-1, 0, 1]
        for x in verticies:
            for y in verticies:
                for z in verticies:
                    sponge = abs(x) + abs(y) + abs(z);
                    # you can try sponge <= 1 to get kinda of
                    # the invert of the menger sponge
                    if sponge > 1:
                        c_scale = self.scale/3
                        x_pos = self.position.x + x * c_scale
                        y_pos = self.position.y + y * c_scale
                        z_pos = self.position.z + z * c_scale
                        cube = Cube(x_pos, y_pos, z_pos, c_scale)
                        cubes.append(cube)
        return cubes

    def displayCube(self):
        with push_matrix():
            stroke(20)
            translate(self.position.x, self.position.y, self.position.z)
            fill(147, 185, 201)
            box(self.scale, self.scale,self.scale)
