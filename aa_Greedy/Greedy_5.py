n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 무게 1~10까지 몇개의 공이 있는가?
array = [0] * 11

for ball in balls:
    array[ball] += 1

count = 0
for i in range(1, m+1):
    n = n - array[i]
    count = count + (array[i] * n)

print(count)