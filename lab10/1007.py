num = int(input())
per = float(input())
num_stu = int(input())
nottest = []
score = []
i = 0
while i < num_stu:
    x = int(input())
    suc = (x/num)*100
    score.append(suc)
    if suc < per:
        nottest.append(suc)
    i += 1
print(len(nottest))
i = 1
j = 0
while i <= num_stu:
    if score[j] >= per:
        print(f'{i} {score[j]:.2f}')
    else:
        print(f'({i}) {score[j]:.2f}')
    i += 1
    j +=1