def card_result(card):
    if card in ['J', 'Q','K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)
    
n = int(input())
if n >= 1 and n <= 100:   
    card_case = []
    for i in range(n):
        card_c = str(input())
        card_case.append(card_c)
    
    output = []
    for case in card_case:
        a = case.split(' ')
        summ = 0
        c = 0
        for card in a:
            summ += card_result(card)
            c += 1
            if summ > 16 or c == 5:
                break
        if summ > 21:
            output.append('busted')
        else:
            output.append(summ)
        
    for o in output:
        print(o)    

