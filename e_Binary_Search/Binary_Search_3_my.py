""" 부품찾기(이진탐색 안 쓴 내 풀이) p.197 """

n = int(input())
tools = list(map(int, input().split()))

m = int(input())
customer_tools = list(map(int, input().split()))

for i in range(len(customer_tools)):
    for j in range(len(tools)):
        if tools[j] == customer_tools[i]:
            print("yes", end=' ')
            break
        else:
            if j == n-1:
                print("no", end=' ')

""" 일단은 맞는거 같음 """
