'''
곱하기 혹은 더하기 p.312

각 자리가 숫자 0-9로 이루어진 문자열 S가 존재
왼쪽에서 오른쪽으로 하나씩 확인하며 숫자 사이에 X or + 를 넣어 가장 큰 수를 구하라
일반적인 사칙연산과 달리 모든 연산은 왼쪽에서 오른쪽이다.
EX) 02984 -> ((((0+2) * 9) * 8) * 4) = 576

입력           출력
02984         576
'''

s = input()

datas = []
for i in s:
    datas.append(int(i))

result = datas[0]
for i in range(1, len(datas)):
    next_num = datas[i]
    if next_num <= 1 or result <= 1:
        result = result + next_num
    else:
        result = result * next_num

print(result)