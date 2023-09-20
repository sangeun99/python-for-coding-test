# 숫자 카드 게임

# N: 행의 개수
# M: 열의 개수

N, M = map(int, input().split())
M_list = []

# 행별로 가장 작은 것의 값을 저장하고 그게 가장 큰 것을 선택해야 함
for _ in range(N):
  N_list = list(map(int, input().split()))
  N_min = min(N_list)
  M_list.append(N_min)
print(max(M_list))
