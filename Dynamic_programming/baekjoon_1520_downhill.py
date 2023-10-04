"""
내리막 길
https://www.acmicpc.net/problem/1520

제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 
항상 내리막길로만 이동하는 경로의 개수 print

오른쪽 아래까지 가기 위해 반복하는 걸 반복해야 함 => dfs
더이상 갈 길이 없을 때 반복이 끝나기.
메모이제이션 사용
"""
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)] # 메모이제이션

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(y, x):
  #목적지에 도달하면 메모에 1 더하도록.
  #dp 상의 목적지를 -1로 냅두는 것이 중요..
  if y==M-1 and x==N-1: 
    return 1

  if dp[y][x] == -1:
    dp[y][x] = 0 #방문표시

    for dy, dx in direction:
      ny = y+dy
      nx = x+dx

      if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] != 0 and graph[y][x] > graph[ny][nx]:
        dp[y][x] += dfs(ny, nx)
  
  return dp[y][x]

print(dfs(0,0))
