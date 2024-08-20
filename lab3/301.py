w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
b = w / h**2
print(f"BMI is {b:.1f}")
if b < 18.5:
    print("Underweight")
elif b > 18.5 and b < 25:
    print("Normal weight")
elif b > 25 and b < 30:
    print("Overweight")
elif b > 30:
    print("Obesity")
