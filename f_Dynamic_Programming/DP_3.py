""" 개미 전사 p.220 """

n = int(input())
food = list(map(int, input().split()))
data = [0] * 100

data[0] = food[0]
data[1] = max(food[0], food[1])

for i in range(2, n):
    data[i] = max(data[i-1], data[i-2] + food[i])

print(data[n-1])