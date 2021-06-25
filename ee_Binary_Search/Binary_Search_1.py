from bisect import bisect_right, bisect_left

n, x = map(int, input().split())
data = list(map(int, input().split()))

result = bisect_right(data, x) - bisect_left(data, x)
if result != 0:
    print(result)
else:
    print(-1)