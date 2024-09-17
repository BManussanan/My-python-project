score = []
i = 0
while i<20:
    num = int(input('Enter score: '))
    if num > 10 or num < 0:
        print('Score is out of range.')
    else:
        score.append(num)
        i += 1
    
print('Original list:')
print(score)
for i in range(11):
    c = 0
    for scores in score:
        if i == scores:
            c += 1
    print(f'{i:>2} {"*" * c}')