""" 연구소 p.341 """
from itertools import combinations
import copy

n, m = map(int, input().split())

lab_map = []
for i in range(n):
    lab_map.append(list(map(int, input().split())))

# combinations 함수를 통해 전체 0의 개수에서 3개 pick하는 좌표의 모든 경우
list_zero = []
for i in range(n):
    for j in range(m):
        if lab_map[i][j] == 0:
            list_zero.append([i, j])
list_zero_c = list(combinations(list_zero, 3))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def spread_virus(x, y, temp):
    for virus_i in range(4):
        nx = x + dx[virus_i]
        ny = y + dy[virus_i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if temp[nx][ny] == 1:
            continue
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            spread_virus(nx, ny, temp)


result = []
for idx_1 in range(len(list_zero_c)):
    temp = copy.deepcopy(lab_map)
    score = 0

    # 벽 세우고
    for idx_2 in range(3):
        a = list_zero_c[idx_1][idx_2][0]
        b = list_zero_c[idx_1][idx_2][1]
        temp[a][b] = 1

    # 바이러스 퍼뜨리고
    for temp_i in range(n):
        for temp_j in range(m):
            if temp[temp_i][temp_j] == 2:
                spread_virus(temp_i, temp_j, temp)

    # 0인 공간 카운트
    for cnt_i in range(n):
        for cnt_j in range(m):
            if temp[cnt_i][cnt_j] == 0:
                score += 1

    result.append(score)

print(max(result))
