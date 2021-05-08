""" 떡볶이 떡 만들기 p.201 """

n, m = list(map(int, input().split()))
rice_cakes = list(map(int, input().split()))

start = 0
end = max(rice_cakes)

result = 0
while start <= end:
    mid = (start + end) // 2
    total_length = 0
    for i in rice_cakes:
        if mid < i:
            total_length = total_length + (i - mid)

    if total_length < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)