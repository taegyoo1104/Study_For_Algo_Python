""" 문자열 재정렬 p.322 """

s = list(input())
s.sort()


count = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        count += 1

result = 0
for i in range(count):
    result += int(s[i])

new_s = "".join(s[count:len(s)+1]) + str(result)
print(new_s)