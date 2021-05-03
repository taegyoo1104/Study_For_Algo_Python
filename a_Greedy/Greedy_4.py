""" 1이 될 때까지  p.99 """

n, k = map(int, input().split())
count = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n = n // k
        count = count + 1
        if n == 1:
            break
    else:
        n = n - 1
        count = count + 1

print(count)