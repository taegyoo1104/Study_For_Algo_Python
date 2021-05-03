""" 큰 수의 법칙  p.92 """

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort()
first = data[n - 1]
second = data[n - 2]

while True :
    if m == 0 : break

    for i in range(k) :
        result = result + first
        m -= 1

    result = result + second
    m -= 1

print(result)