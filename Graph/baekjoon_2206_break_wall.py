"""
벽 부수고 이동하기
https://www.acmicpc.net/problem/2206

규칙:
1. (N, M)까지 못 갈 경우 -1
2. (1,1)과 (N,M)은 둘 다 0임
3. 시작, 끝나는 칸도 세기. => 최단경로가 최소 2임.
4. 이동 가능 칸: 상하좌우
5. 벽은 한 개만 부술 수 있음

방법
벽을 부수는 모든 경우의 수 따져야 하나.. 
- 1을 하나씩만 다 없애봐야하나.... => 일단 이렇게 해보기


6 4
0100
1110
1000
0000
0111
0000

15
"""
import copy
from collections import deque

N, M = list(map(int, input().split()))
field_input = [list(map(int, ''.join(input().split()))) for _ in range(N)]

shortest = float("inf")
visited = [[0 for _ in range(M)] for _ in range(N)]

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우

def isMovable(field, visit_arr, nxt):
  y, x = nxt
  # 맵의 범위에서 벗어나는가
  if (y > N-1 or x > M-1 or y < 0 or x < 0):
    return False
  # 갈 위치가 벽이거나 방문했던 곳인가
  if (field[y][x] == 1 or visit_arr[y][x] > 0):
    return False
  return True

# 시작을 늘 (0,0)에서 하는 bfs
def bfs(field):
  visited[0][0] = 1
  queue = deque([[0,0]])

  while queue:
    y, x = queue.popleft()

    if [y, x] == [N-1, M-1]:
      return visited[y][x]

    for dy, dx in direction:
      ny = y+dy
      nx = x+dx

      if isMovable(field, visited, [ny, nx]):
        visited[ny][nx] = visited[y][x] + 1
        queue.append([ny, nx])

  return float('inf')
      
for r in range(N):
  for c in range(M):
    if field_input[r][c] == 1:
      field_copy = copy.deepcopy(field_input)
      field_copy[r][c] = 0
    
      shortest = min(shortest, bfs(field_copy))
      #print('shortest :::', shortest)
      #print('===============copy map bfs complete==============')
  
print(shortest if(shortest < float('inf')) else -1)

