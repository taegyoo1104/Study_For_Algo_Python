""" 상하좌우 p.110 """

n = int(input())
movings = input().split()  # list에 들어감
moving_Types = ['L', 'R', 'U', 'D']
# 시작점
x = 1
y = 1

# LRUD 좌표 움직임
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for moving in movings:
    for i in range(4):
        if moving == moving_Types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if (nx < 1 or ny < 1) or (nx > n or ny > n):
        continue
    x = nx
    y = ny

print(x, y)