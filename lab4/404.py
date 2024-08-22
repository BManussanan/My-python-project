ch = input("Enter your buffet choice: ")
if ch == 'Korean':
    wed = input("Is today Wednesday (yes/no)? ")
    if wed == 'yes':
        price = 1500*85/100
        print(f"Your payment is {price:.2f} Baht.")
    else:
        price = 1500
        print(f"Your payment is {price:.2f} Baht.")        
elif ch == 'Japanese':
    wed = input("Is today Wednesday (yes/no)? ")
    if wed == 'yes':
        price = 1000*85/100
        print(f"Your payment is {price:.2f} Baht.")
    else:
        price = 1000
        print(f"Your payment is {price:.2f} Baht.")     
elif ch != 'Japanese' and ch != 'Korean':
    print(f"Sorry, there is no {ch} buffet.")
    
    
