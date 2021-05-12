'''
만들 수 없는 금액 p.314

N개의 동전을 이용해 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하라

EX)
N = 5 각각 3 2 1 1 9원 이라면 만들 수 없는 양의 정수 금액 중 최솟값은 8원이다

입력          출력
5            8
2 3 1 1 9
'''

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

price = 1
for coin in coins:
    if coin > price:
        break
    price += coin

print(price)