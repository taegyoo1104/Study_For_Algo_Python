""" 시각  p.113 """

n = int(input())
count3 = 0;

for i in range(n+1):
    for min in range(60):
        for sec in range(60):
            if '3' in str(i) + str(min) + str(sec):
                count3 = count3 + 1

print(count3)