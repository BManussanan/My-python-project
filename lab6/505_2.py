n = int(input('Enter height: '))
i = 0
while i < n:
    j = (n-i-1)*2
    while j > 0:
        print(' ', end="")
        
        j -= 1
    print('1', end="")
    j = 0
    while j < i*2:    
        print(' ', end="")
        
        j += 1
        while j < i*2:    
            print(' ', end="")
            
            j += 1
        print(' '*(j-1), end="")    
        print('1', end="")       
    print()
    i+=1