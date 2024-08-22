price = float(input("Enter buying amount: "))
if price >= 1000 and price < 3000:
        total = price*90/100
        print(f"Amount due after discount is {total:.2f} baht.")        
elif price >= 3000:
        total = price*85/100
        print(f"Amount due after discount is {total:.2f} baht.")
else:
        print(f"Amount due after discount is {price:.2f} baht.")
