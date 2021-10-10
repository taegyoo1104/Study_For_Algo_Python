"""
1~5개 양방향 노드/ 1에서 3 으로 갈 때 가장 적은 cost
"""
import heapq
INF = int(1e9)
distance = [INF] * (5+1)

graph_info = [[1, 2, 1000], [1, 5, 2000], [2, 3, 3000], [2, 4, 1500], [3, 4, 1000], [4, 5, 2000]]
graph = [[] for _ in range(5+1)]
for value in graph_info:
    a, b, c = value[0], value[1], value[2]
    graph[a].append((b, c))
    graph[b].append((a, c))

h = []
heapq.heappush(h, (0, 1))
distance[1] = 0
while h:
    dist, now = heapq.heappop(h)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(h, (cost, i[0]))

print(distance[3])