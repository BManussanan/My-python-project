tv = int(input("How many TVs? "))
player = int(input("How many DVD players? "))
audio = int(input("How many Audio Systems? "))
price = 6000*tv+1500*player+3000*audio 
print(f"Total price is {price:.2f} baht.")
if price < 24000:
    total = price
    print(f"Your payment is {total:.2f} baht. Thank you!")    
else :
    total = price*80/100  
    discount = price*20/100
    print(f"You've got a discount of {discount:.2f} baht.")
    print(f"Your payment is {total:.2f} baht. Thank you!")    
