'''
문자열 뒤집기 p.508

0과 1로 이루어진 문자열 S
문자열 S에 있는 모든 숫자를 전부 같게 만들고 싶다.
S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
1 -> 0  0 -> 1
EX)
0001100
1. 전체를 뒤집으면 1110011
2. 4,5번을 뒤집으면 1111111
하지만 처음부터 4,5번을 뒤집으면 0000000 -> 1번 만에 같은 숫자로 만들 수 있음
행동의 최소 횟수를 구하라

입력          출력
0001100      1
'''

s = input()
count_change_to_0, count_change_to_1 = 0, 0

if s[0] == '0':
    count_change_to_1 += 1
else:
    count_change_to_0 += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            count_change_to_1 += 1
        else:
            count_change_to_0 += 1

print(min(count_change_to_0, count_change_to_1))