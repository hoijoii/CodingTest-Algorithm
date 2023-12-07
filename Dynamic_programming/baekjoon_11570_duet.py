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
music = [0] + list(map(int, input().split())) #0은 노래 시작 전 초기상태. 노래는 인덱스1부터
dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)] #둘 중 맨처음 부르는 경우의 수(dp[0][i]랑 dp[i][0])도 고려해야 해서 N+1
answer = float('inf')

dp[0][1], dp[1][0] = 0, 0

for a in range(N+1):
  for b in range(N+1):
    if a==b: continue

    nxt = max(a, b) + 1 #마지막 부른 음의 다음 음
    if nxt > N: continue

    diff = 0 if a==0 else abs(music[a]-music[nxt]) # a가 아예 노래를 안 불렀던 경우 차를 구할 필요 없으니 0
    dp[nxt][b] = min(dp[nxt][b], dp[a][b] + diff) # a가 다음 음을 부르는 경우

    diff = 0 if b==0 else abs(music[b]-music[nxt]) # b가 아예 노래를 안 불렀던 경우 차를 구할 필요 없으니 0
    dp[a][nxt] = min(dp[a][nxt], dp[a][b] + diff) # b가 다음 음을 부르는 경우

for i in range(N):
  answer = min(answer, dp[i][N]) 

print(answer)
