"""
퇴사2
https://www.acmicpc.net/problem/15486

N=퇴사날짜까지 남은 날
N+1=퇴사날
T=상담하는데 걸리는 일수
P=금액
하루에 할 수 있는 상담은 하나

정답=얻을 수 있는 최대 수익
T가 제일 큰 것부터 시도해봐야 빨리 찾는 거 아님?
조건: N-idx >= T 남은 날짜 수보다 T가 같거나 작아야 상담이 가능함

7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

45
점화식 ,,
dp[i + T] = max(dp[i + T], dp[i] + P)
"""
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = {}

for idx, item in enumerate(schedule):
  t, p = item
  


""" schedule_T = []
schedule_P = []

for i in range(N):
  t, p = list(map(int, input().split()))
  schedule_T.append(t)
  schedule_P.append(p)

dp = [0]*N
min_t = 51
max_p = 0

print(schedule_T)
print(schedule_P)

for idx, val in enumerate(schedule_P):
  if schedule_T[idx] <= N-idx:
    
 """
  """ if val <= N-idx:
    min_t = min(val, min_t) """