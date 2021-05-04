""" 음료수 얼려 먹기  p.149 """

n, m = map(int, input().split())

icebox = []
for i in range(n):
    icebox.append(list(map(int, input())))

def dfs(x, y):
    if (x < 0 or y < 0) or (x >= n or y >= m): return False

    if icebox[x][y] == 0:
        icebox[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x, y - 1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)