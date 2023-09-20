# 1이 될 때까지

# N에서 1을 빼거나 N을 K로 나누거나
# 1이 될 때까지 최소 횟수 구하기

N, K = map(int, input().split())
count = 0

while True:
  if (N == 1):
    break
  else:
    if (N % K == 0):
      N //= K
    else:
      N -= 1
    count += 1
print(count)
