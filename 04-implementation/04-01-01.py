# 상하좌우

def is_valid(x, y, N):
  if (x < 1 or y < 1):
    return False
  elif (x > N or y > N):
    return False
  else:
    return True

# L(0) R(1) U(2) D(3)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
move_list = list(input().split())

cur_x = 1
cur_y = 1

for m in move_list:
  if m == "L" :
    new_x  = cur_x + dx[0]
    new_y  = cur_y + dy[0]
  elif m == "R" :
    new_x  = cur_x + dx[1]
    new_y  = cur_y + dy[1]
  elif m == "U" :
    new_x  = cur_x + dx[2]
    new_y  = cur_y + dy[2]
  else :
    new_x  = cur_x + dx[3]
    new_y  = cur_y + dy[3]
  if is_valid(new_x, new_y, N):
    cur_x = new_x
    cur_y = new_y

print(cur_x, cur_y)