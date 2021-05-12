score = input()
mid_index = (len(score)-1) // 2

score_front = score[0: mid_index+1]
score_back = score[mid_index+1: len(score)+1]

result1, result2 = 0, 0
for i in range(0, len(score_front)):
    result1 += int(score_front[i])
    result2 += int(score_back[i])


if result1 == result2:
    print('LUCKY')
else:
    print('READY')