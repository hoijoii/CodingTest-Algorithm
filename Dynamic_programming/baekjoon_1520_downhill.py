"""
내리막 길
https://www.acmicpc.net/problem/1520

제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 
항상 내리막길로만 이동하는 경로의 개수 print

오른쪽 아래까지 가기 위해 반복하는 걸 반복해야 함
더이상 갈 길이 없을 때 반복이 끝나기.

갈림길의 수를 그 위치에 숫자로 표시
or
bfs처럼..? 재귀로 들어가기 
or
dfs: 루트를 몇 번 더 반복해야 하니 시간 초과 부담,,
"""
M, N = map(int, input().split())
graph = [[map(int, input().split())] for _ in range(M)]
route = [[-1 for _ in range(N)] for _ in range(M)]
count = 0

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] 

def dfs(y, x):
  global count
  
  if y==M and x==N:
    count+=1
    return
  
  if route[y][x] == 0:
    for dy, dx in direction:
      ny = y+dy
      nx = x+dx
      if 0 <= ny < M and 0 <= nx < N and graph[y][x] > graph[ny][nx]:
        

""" def move(x, y):
  global count
  print(y, x)
  for dy, dx in direction:
    ny = y+dy
    nx = x+dx

    if y == M-1 and x == N-1:
      count+=1
      print('============================')
      continue
    
    if 0 <= ny < M and 0 <= nx < N:
      if graph[y][x] > graph[ny][nx]: 
        move(nx, ny)
      else:
        continue

move(0, 0)
  
print(count) """



""" for r in range(M):
    for c in range(N):
      move(c, r) """
    