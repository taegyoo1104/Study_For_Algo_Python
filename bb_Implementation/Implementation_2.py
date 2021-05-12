datas = input()

result = []
value = 0
for data in datas:
    if data.isalpha():
        result.append(data)
    else:
        value += int(data)

if value == 0:
    print(''.join(result))
else:
    result.append(str(value))
    print(''.join(result))