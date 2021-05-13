""" 특정 거리의 도시 찾기 p.530 """
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


visited = [-1] * (n+1)
visited[x] = 0

queue = deque()
queue.append(x)
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = visited[v] + 1
            queue.append(i)

check = False
for i in range(len(visited)):
    if visited[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

