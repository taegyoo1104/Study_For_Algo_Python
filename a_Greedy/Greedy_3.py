""" 숫자 카드 게임  p.96 """

n, m = map(int, input().split())
result = 0

""" 1번 풀이 min() function """
'''
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(min_value, result)

print(result)

'''

""" 2번 풀이 2중 for """
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001

    for j in data:
        min_value = min(min_value, j)
    result = max(min_value, result)

print(result)