""" 부품 찾기 p.197 """

def search_tool(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return search_tool(array, target, start, mid - 1)
    else:
        return search_tool(array, target, mid + 1, end)

n = int(input())
tools = list(map(int, input().split()))
m = int(input())
customer = list(map(int, input().split()))

tools.sort()

for i in range(m):
    result = search_tool(tools, customer[i], 0, n - 1)
    if result is not None:
        print("yes", end=' ')
    else:
        print("no", end=' ')