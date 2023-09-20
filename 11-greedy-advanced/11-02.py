# 곱하기 혹은 더하기

s = input()

result = 0
exception = [0, 1]

for i in range(len(s)):
  if result in exception or int(s[i]) in exception:
    result = result + int(s[i])
  else:
    result *= int(s[i])

print(result)