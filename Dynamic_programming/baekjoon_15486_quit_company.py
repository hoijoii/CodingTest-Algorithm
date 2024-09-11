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
dp = [0] * (N+1) # (index)일까지 얻을 수 있는 최대 수익 기록

for idx, item in enumerate(schedule):
  t, p = item
  dp[idx] = max(dp[idx-1], dp[idx]) # 지금까지 최대 수익을 정함(dp[idx-1]: 어제까지의 최대수익, dp[idx]: 0 혹은 점화식으로 계산해서 나온 수익)

  # 상담을 정해진 날짜 안에 마칠 수 있는지
  if idx + t <= N:
    # 오늘부터 상담을 시작하고 나서 i+t일에 얻을 수 있는 수익 기록.
    # dp[idx+t]: 기존에 점화식으로 계산되어 나온 놈 or 0
    # dp[idx]+p: 지금까지의 최대 수익에 상담진행했을 때 수익을 더한 넘
    dp[idx+t] = max(dp[idx+t], dp[idx]+p) 

print(max(dp[N-1], dp[N])) # dp[N]이 비어있을 수 있으므로 둘 중에 큰 값 선택.




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