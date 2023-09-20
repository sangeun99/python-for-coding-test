# 큰 수의 법칙

N, M, K = map(int, input().split())
N_list = list(map(int, input().split()))
sum = 0
k_count = 0

N_list.sort()
N_list.reverse()

for _ in range(M):
  if (k_count < K) :
    sum += N_list[0]
    k_count += 1
  else :
    sum += N_list[1]
    k_count = 0
print(sum)