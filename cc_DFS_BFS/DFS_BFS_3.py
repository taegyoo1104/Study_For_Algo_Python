from collections import deque

n, k = map(int, input().split())

test_map = []
data = []
for i in range(n):
    test_map.append(list(map(int, input().split())))
    for j in range(n):
        if test_map[i][j] != 0:
            # 바이러스 번호, 시간, x축, y축
            data.append((test_map[i][j], 0, i, j))


s, targetX, targetY = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


data.sort()
queue = deque()
for i in data:
    queue.append(i)

while queue:
    virus_number, sec, x, y = queue.popleft()
    if sec == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if test_map[nx][ny] == 0:
            test_map[nx][ny] = virus_number
            sec += 1
            queue.append((virus_number, sec, nx, ny))

print(test_map[targetX-1][targetY-1])
