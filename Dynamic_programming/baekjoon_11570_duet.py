"""
환상의 듀엣
https://www.acmicpc.net/problem/11570

abs(현재음-직전에부른음)이 최소화돼야함.
모든 경우를 다 봐야 하니까 dp 사용하기
dp[i][j]: i번째는 상덕, j번째는 희원이 마지막으로 불렀을 때 가질 수 있는 최소값

max(i, j) : i, j 중 마지막으로 불려진 음
희원: dp[i][j] + abs(music[j]-music[max(i, j)])
"""
N = int(input())
music = list(map(int, input().split()))
dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
answer = float('inf')

dp[0][1], dp[1][0] = 0, 0

for a in range(N+1):
  for b in range(N+1):
    if a==b: continue

    nxt = max(a, b) + 1 #마지막 부른 음의 다음 음
    if nxt >= N: continue

    """ if a==0 or b==0:
      music[0] = music[nxt] # 0이면 음이 바뀌는 cost가 없음. abs를 0으로 만들기 """

    dp[nxt][b] = min(dp[nxt][b], dp[a][b] + abs(music[a]-music[nxt]))
    dp[a][nxt] = min(dp[a][nxt], dp[a][b] + abs(music[b]-music[nxt]))
    print(a, b, nxt, dp[nxt][b], dp[a][nxt])
  print('===============================')
  print(dp)

for i in range(N):
  answer = min(answer, dp[i][N-1])
  answer = min(answer, dp[N-1][i])

print(answer)

"""
5
1 3 8 12 13
7
"""