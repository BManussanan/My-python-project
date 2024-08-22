w=float(input("Enter width: "))
l=float(input("Enter length: "))
d=float(input("Enter depth: "))
total=(w*l*d*15)/60
output = "Time to fill a pool is {0:.2f} minutes.".format(total)
print(output)
