""" 성적이 낮은 순서로 학생 출력  p.180 """

n = int(input())
data = []

for i in range(n):
    array = input().split()
    data.append((array[0], int(array[1])))

data = sorted(data, key=lambda student: student[1])

for student in data:
    print(student[0], end=' ')