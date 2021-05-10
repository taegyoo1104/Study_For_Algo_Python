'''
모험가 길드 p.311

모험가 N명 각각은 '공포도'가 있다.
그룹을 구성하기 위해서 공포도가 X인 모험가가 포함된 그룹은 반드시 X명 이상으로 구성해야한다.
몇 명의 모험가는 마을에 남아도 된다. 모든 모험가를 그룹에 넣을 필요는 없음
최대 몇 개의 그룹 구성 가능?
EX)
N = 5
공포도
2 3 1 2 2

그룹1 -> 1 2 3
그룹2 -> 2 2
총 2개의 그룹

입력                   출력
5                     2
2 3 1 2 2
'''

n = int(input())
datas = list(map(int, input().split()))
group = 0
count_person = 0

datas.sort()

for data in datas:
    count_person = count_person + 1
    if data >= count_person:
        group = group + 1
        count_person = 0

print(group)