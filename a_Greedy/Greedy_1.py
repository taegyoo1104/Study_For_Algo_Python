""" 동전문제  p.88 """

price = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coins in coin_types:
    count += (price // coins)
    price = price % coins

print(count)