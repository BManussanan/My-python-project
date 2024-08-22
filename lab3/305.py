target = 72
num = int(input("Enter your guess (0 - 100): "))
if num >= 0 and num <= 100:
    if num == target:
        print("Congratulations, your guess is correct.")
    else :
        print("Sorry, your guess is wrong, try again later.")
else :
    print("Sorry, out of range, try again later.")
