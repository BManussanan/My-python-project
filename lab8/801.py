import math
def circle(x):
    area = math.pi*math.pow(x,2)
    return area
def circumference(x):
    cir = math.pi*2*x
    return cir
def sphere(x):
    sp = 4/3*math.pi*math.pow(x,3)
    return sp
r = float(input('Enter a radius: '))

print('Area of a circle with radius {:.2f} is {:.2f}.'.format(r, circle(r)))
print('Circumference of a circle with radius {:.2f} is {:.2f}.'.format(r, circumference(r)))
print('Volume of sphere with radius {:.2f} is {:.2f}.'.format(r, sphere(r)))