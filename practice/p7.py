choice = input("Select menu (A, B): ")
if (choice in 'Aa'):
    print('This is menu A')
elif (choice in 'Bb'):
    print('This is menu B')
else:
    print('Invalid menu: neither A nor B')