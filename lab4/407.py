l = int(input("Enter level pokemon: "))
ball = input("Enter level pokeball: ")
d = int(input("Enter distance: "))
x = 0
if ball == 'h' or ball == 'H':
    if l >= 0 and l <= 40:
        x = 0.01
    elif l >= 41 and l <= 60:
        x = 0.01
    elif l >= 61 and l <= 100:
        x = 0.01
elif ball == 'm' or ball == 'M':
    if l >= 0 and l <= 40:
        x = 0.03
    elif l >= 41 and l <= 60:
        x = 0.05
    elif l >= 61 and l <= 100:
        x = 0.08
elif ball == 'l' or ball == 'L':
    if l >= 0 and l <= 40:
        x = 0.05
    elif l >= 41 and l <= 60:
        x = 0.03
    elif l >= 61 and l <= 100:
        x = 0.1
s = 100 - (l*d*x)
if s < 0.00 or s > 100.00 :
    print("0.00 percent.")
else:
    print(f"{s:.2f} percent.")
