# 왕실의 나이트

# 나이트의 이동 경로 총 8군데
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
alph_to_int = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

cur = input()
cur_x = alph_to_int.index(cur[0]) + 1
cur_y = int(cur[1])

count = 0
for i in range(8):
  x = cur_x + dx[i]
  y = cur_y + dy[i]
  if x >= 1 and y >= 1 and x <= 8 and y <= 8 :
    count += 1
  
print(count)