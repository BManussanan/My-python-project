import math
def find_sd(l):
    average = sum(l)/len(l)
    i = 0
    total = 0
    while i < len(l):
        total += math.pow(l[i]-average,2)
        i += 1
    return math.sqrt(total/(len(l)-1))
score = []
while True:
    num = float(input('Enter score: '))
    if num == -1:
        break
    if num > 100 or num < 0:
        print('Score is out of range.')
    else:
        score.append(num)
if len(score) != 0:
    a = sum(score)/len(score)
    print(f'Maximum score is {max(score):.2f}.')
    print(f'Minimum score is {min(score):.2f}.')
    print(f'Average score is {a:.2f}.')
    print(f'Standard deviation is {find_sd(score):.2f}.')
