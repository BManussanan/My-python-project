def card(sta):
    sample = []
    for i in sta:
        if i in ['J','K','Q']:
            sample.append(10)
        elif i == 'A':
            sample.append(1)
        else:
            sample.append(int(i))
    return sample

def maxx_card(f):
    maxx = 0
    max_keys = ''
    c = 0
    summ_sort = 0
    card_sort = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                 '8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    for i in f:
        if summ_sort > 16 or c == 5:
            break
        summ_sort += card_sort[i]
        c += 1
        if card_sort[i] > maxx:
            maxx = card_sort[i]
            max_keys = i
    return max_keys

def summ_card(s):
    summ = 0
    c = 0
    for i in s:
        c += 1
        summ += i
        if summ > 16 or c == 5:
            break
    if summ > 21:
        return 'busted'
    else:
        return summ
    
state = input().split()
print(maxx_card(state))
print(summ_card(card(state)))
