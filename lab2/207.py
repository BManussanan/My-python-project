import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))
a1 = math.pow(x,y) + z
a2 = math.cos(2*math.pi) + math.log(x,math.e)
a3 = abs(x)+abs(y)
a4 = math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2))
a5 = math.pow(math.sin(x),2)+math.pow(math.cos(x),2)
a6 = math.pow(x+y,1/5)
a7 = math.pow(math.e,math.log(math.pow(y,x)))
print("a1 = " + f"{a1:.2f}")
print("a2 = " + f"{a2:.2f}")
print("a3 = " + f"{a3:.2f}")
print("a4 = " + f"{a4:.2f}")
print("a5 = " + f"{a5:.2f}")
print("a6 = " + f"{a6:.2f}")
print("a7 = " + f"{a7:.2f}")
