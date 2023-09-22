# 구현 문제

### 개요
- 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
- 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
- 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
- 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
- 적절한 라이브러리를 찾아서 사용해야 하는 문제

### 시뮬레이션 및 완전 탐색 문제
- 2차원 공간에서의 방향 벡터가 자주 활용됨
```
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
  nx = x + dx[i]
  ny = y + dy[i]
  print(nx, ny)
```

### 완전탐색문제
- 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
- 예시 : [시각 문제](https://github.com/sangeun99/python-for-coding-test/blob/master/04-implementation/04-01-02.py)
- 하루는 86400초이므로 모든 경우에서 확인 후 풀이해도 됨

### 문제 풀기
- [상하좌우](https://github.com/sangeun99/python-for-coding-test/blob/master/04-implementation/04-01-01.py)
- [시각](https://github.com/sangeun99/python-for-coding-test/blob/master/04-implementation/04-01-02.py)
- [왕실의 나이트](https://github.com/sangeun99/python-for-coding-test/blob/master/04-implementation/04-02.py)
- [문자열 재정렬](https://github.com/sangeun99/python-for-coding-test/blob/master/11-implementation-advanced/12-08.py)

### 문제 풀이 중 얻은 힌트
- ASCII 코드 사용하여 char to int 구현하기
```
num = int(ord(character)) - int(ord('a'))
```
- 리스트에 있는 값들을 문자열으로 이어붙이는 방법
```
''.join(r)
```