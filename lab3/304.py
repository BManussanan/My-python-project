price = float(input("Total Price: "))
if price < 50 :
    print(f"You got: {0}")
else :
    total = price//50
    print(f"You got: {total:.0f}")
