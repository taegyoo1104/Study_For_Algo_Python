def binary_s(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return binary_s(arr, mid+1, end)
    else:
        return binary_s(arr, start, mid-1)

n = int(input())
data = list(map(int, input().split()))

if binary_s(data, 0, n - 1) is None:
    print(-1)
else:
    print(binary_s(data,0, n-1))