# 문자열 재정렬

string = input()
s_list_alphabet = []
sum = 0
result = ''

for i in string:
  if i.isdigit():
    sum += int(i)
  else :
    s_list_alphabet.append(i)
s_list_alphabet.sort()

for i in s_list_alphabet:
  result += i
if result != 0:
  result += str(sum)

print(result)