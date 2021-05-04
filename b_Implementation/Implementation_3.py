""" 왕실의 나이트  p.115 """

data = input()
count = 0

row = int(data[1]) # x
col = ord(data[0]) - ord('a') + 1 # y


movings = [(-2, -1), (-2, 1),
          (-1, 2), (1, 2),
          (2, 1), (2, -1),
          (1, -2), (-1, -2)]

for i in range(len(movings)):
    nrow = row + movings[i][0]
    ncol = col + movings[i][1]

    if (nrow < 1 or ncol < 1) or (nrow > 8 or ncol > 8):
        continue
    count += 1

print(count)