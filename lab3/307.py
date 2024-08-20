import math
x = float(input("Enter x : "))
y = 0 
if x < 0 :
    y = math.sqrt(x**2+1)
    print(f"f({x:.2f}) = {math.ceil(y)}")
elif x == 0 :
    y = x
    print(f"f({x:.2f}) = {math.ceil(y)}")
elif 0 < x <= 99 :
    y = 3*x**2 - (1-x)**2
    print(f"f({x:.2f}) = {math.ceil(y)}")
elif x > 99 :
    y = 2*math.pow(x,3)-x/math.sqrt(x + 1)
    print(f"f({x:.2f}) = {math.ceil(y)}")
