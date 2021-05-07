""" 위에서 아래로  p.178 """

n = int(input())
datas = []

for i in range(n):
    datas.append(int(input()))

datas = sorted(datas, reverse=True)

for data in datas:
    print(data, end=' ')