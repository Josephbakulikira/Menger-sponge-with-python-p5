from p5 import *
from Cube import Cube
angle =0

c = Cube(0, 0, 0, 800)
cubes = []
cubes.append(c)
recursion_limit = 2
counter = 0
def setup():
    size(1000, 1000)

def mouse_pressed():
    global cubes, counter, recursion_limit
    if counter < recursion_limit:
        recursion = []
        for cube in cubes:
            menger = cube.generate()
            recursion.extend(menger)
        cubes = recursion
        counter += 1
    else:
        print("you've reached the recursion limit")
def draw():
    global angle
    background(0)
    stroke(255)
    no_fill()
    rotate_y(angle)
    for cube in cubes:
        cube.displayCube()
    angle += 0.01;
if __name__ == "__main__":
    run(mode='P3D')
