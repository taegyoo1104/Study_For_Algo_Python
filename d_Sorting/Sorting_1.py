""" Selection Sort  p. 157 """
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# Swap 사용.ver
'''
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index] # swap
'''
# no swap.ver
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp


print(array)

