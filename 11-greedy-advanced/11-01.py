# 모험가의 길드

def makeGroup(N, a_list):
  count = 0
  rest = N
  a_list.sort()
  i = 0
  while i < len(a_list):
    if rest - a_list[i] < 0:
      return count
    else:
      sublist = a_list[i:i+a_list[i]]
      while (sublist[-1] != len(sublist)):
        if rest - sublist[-1] < 0:
          return count
        sublist = a_list[i:i+sublist[-1]]
      print(sublist)

      rest -= sublist[-1]
      i += sublist[-1]
      count += 1
  return count

N = int(input())
a_list = list(map(int, input().split()))

print(makeGroup(N, a_list))