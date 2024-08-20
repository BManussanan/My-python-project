print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")
ch1 = input("Enter your choice: ")
if ch1 == 'B' or ch1 == 'b':
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    ch2 = input("Enter your choice: ")
    if ch2 == 'R' or ch2 == 'r':
        total = 60
        output = "Regular Burger"
        print(f"Your {output} is {total} Baht.")
    elif ch2 == 'C' or ch2 == 'c':
        total = 75
        output = "Cheese Burger"
        print(f"Your {output} is {total} Baht.")
    elif ch2 == 'D'or ch2 == 'd':
        total = 90
        output = "Double Cheese Burger"
        print(f"Your {output} is {total} Baht.")
    else:
        print("Invalid sub menu choice.")   
elif ch1 == 'C' or ch1 == 'c':
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
    ch2 = input("Enter your choice: ")
    if ch2 == 'F' or ch2 == 'f':
        total = 120
        output = "Fried Chicken"
        print(f"Your {output} is {total} Baht.")
    elif ch2 == 'G' or ch2 == 'g':
        total = 150
        output = "Grilled Chicken"
        print(f"Your {output} is {total} Baht.")
    elif ch2 == 'C' or ch2 == 'c':
        total = 180
        output = "Chef's Chicken"
        print(f"Your {output} is {total} Baht.")
    else:
        print("Invalid sub menu choice.")   
elif ch1 == 'P' or ch1 =='p':
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    ch2 = input("Enter your choice: ")
    if ch2 == 'S' or ch2 == 's':
        total = 90
        output = "Spaghetti de Italiano"
        print(f"Your {output} is {total} Baht.")
    elif ch2 == 'L' or ch2 == 'l':
        total = 120
        output = "Lasagna Supreme"
        print(f"Your {output} is {total} Baht.")
    elif ch2 == 'M' or ch2 == 'm':
        total = 100
        output = "Macaroni Special"
        print(f"Your {output} is {total} Baht.")
    else:
        print("Invalid sub menu choice.")
else:
    print("Invalid main menu choice.")
