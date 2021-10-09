""" 간단한 다익스트라 """

import sys

input = sys.stdin.readline()
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())  # 시작 노드의 번호
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)  # 최단 거리 테이블을 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())  # a에서 b로 가는 비용이 c
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호 리턴
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            index = i
    return index


def dijkstra(start):
    # 시작 노드 세팅
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 n-1 개의 노드에 대해 반복
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거펴서 다른 노드로 이동하는 거리가 더 짧을 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])