""" 효율적인 화폐 구성 p.226 """

n, m = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

INF = 100001
dp = [INF] * (m+1)

dp[0] = 0
for coin in coins:
    for i in range(coin, m+1):
        if dp[i - coin] != INF:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[m] == INF:
    print(-1)
else:
    print(dp[m])