exercise = input().split()
e = [int(x) for x in exercise]
percent = input().split()
p = [float(x) for x in percent]
num_stu = int(input())
student_atten = {}
student_score = {}
student = {}
score= {}
for i in range(1,num_stu+1):
    a = input().split()
    num = [int(j) for j in a]
    student_atten[i] = num
for i in range(1,num_stu+1):
    s = input().split()
    num = [int(j) for j in s]
    student_score[i] = num
for i in student_atten:
    total = [sum(student_atten[i])/len(student_atten[i]) * 100]
    student[i] = total
for i in student_score:
    total_2 = [sum(student_score[i])/sum(e) * 100]
    score[i] = total_2
c = 0
for i in range(1,num_stu+1):
    if student[i][0] < p[0] and score[i][0] < p[1]:
        c += 1
print(c)
for i in range(1,num_stu+1):
    if student[i][0] < p[0] and score[i][0] < p[1]:
        print(f'({i}) {student[i][0]:.2f} {score[i][0]:.2f}')
    else:
        print(f'{i} {student[i][0]:.2f} {score[i][0]:.2f}')

