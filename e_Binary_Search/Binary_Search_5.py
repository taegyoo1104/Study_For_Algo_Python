""" bisect(정렬된 리스트에서 해당 값이 몇 번 나옴?) """
from bisect import *

n, m = list(map(int, input().split()))
data = list(map(int, input().split()))


def count_by_range(data, m):
    left_index = bisect_left(data, m)
    right_index = bisect_right(data, m)

    return right_index - left_index


result = count_by_range(data, m)
if result < 0:
    print(-1)
else:
    print(result)
