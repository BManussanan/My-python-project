s = str(input())
st = s.split('x')
m = int(st[0])  # จำนวนแถว
n = int(st[1])  # จำนวนคอลัมน์
table = ''

# เก็บตำแหน่งของ mines (จุดที่เป็น '*')
point = []
num = int(input())  # จำนวน mines
for i in range(num):
    po = str(input())
    point.append(po.split(','))
p = []
for pp in point:
    p.append([int(pp[0]), int(pp[1])])

# สร้างตาราง
for i in range(m):
    for j in range(n):
        if [i, j] in p:
            table += '*'  # วาง mine ที่จุดนี้
        else:
            c = 0  # จำนวน mines รอบๆ จุดนี้
            # วนลูปตรวจสอบ 8 ทิศทางรอบๆ
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue  # ข้ามจุดตรงกลางที่เป็นตัวเอง
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:  # เช็คว่าจุดนั้นอยู่ในตารางหรือไม่
                        if [ni, nj] in p:  # ถ้ามี mine อยู่ในจุดนั้น
                            c += 1
            table += str(c)  # ใส่จำนวน mines รอบๆ
    table += '\n'

print(table)
