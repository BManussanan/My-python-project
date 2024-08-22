import math
r=int(input("Enter a radius: "))
area = math.pi*r**2
circum = math.pi*2*r
output1 = "Area of a circle with radius {0} is {1:.2f}".format(r,area)
output2 = "Circumference of a circle with radius {0} is {1:.2f}".format(r,circum)
print(output1)
print(output2)
