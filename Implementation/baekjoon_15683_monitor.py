"""
감시
https://www.acmicpc.net/problem/15683

1. #를 그릴 때마다 전체 # 개수 세기?
2. #가 먼저 그려졌던 부분은 -1 표시, #를 그릴 때 조건 고려..
  - # 그릴 때마다 count 증가
  - -1이면 #가 안 그려지게끔..
  - count 다 셌으면 최고값 저장하는 변수 갱신(최고값변수보다 count가 작으면 갱신x)
  - 최고값보다 count가 크면 # 그렸던 거 적용, 작으면 이전 office로 되돌림

"""
import copy

M, N = map(int, input().split()) #세로가로
office = [list(map(int, input().split())) for _ in range(M)]
min_val = float('inf')
temp = []
cctv = []

def up(map, x, y):
  for i in range(x-1, -1, -1):
    if map[i][y] == 6: 
      return
    if map[i][y] == 0 : 
      map[i][y] = -1

def down(map, x, y):
  for i in range(x+1, M):
    if map[i][y] == 6: 
      return
    if map[i][y] == 0 : 
      map[i][y] = -1

def left(map, x, y):
  for i in range(y-1, -1, -1):
    if map[x][i] == 6: 
      return
    if map[x][i] == 0 : 
      map[x][i] = -1
  
def right(map, x, y):
  for i in range(y+1, N):
    if map[x][i] == 6: 
      return
    if map[x][i] == 0 : 
      map[x][i] = -1

def counting(map):
  cnt = 0
  for m in range(M):
    for n in range(N):
      if map[m][n] == 0: cnt+=1
  return cnt

def dfs(depth, map, dump):
  if depth == len(cctv):
    global min_val 
    min_val = min(min_val, counting(map))
    return
  
  x, y = cctv[depth]

  if office[x][y] == 1:
    temp = copy.deepcopy(map)
    up(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    down(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    left(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    right(temp, x, y)
    dfs(depth+1, temp, dump)

  elif office[x][y] == 2:
    temp = copy.deepcopy(map)
    up(temp, x, y)
    down(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    left(temp, x, y)
    right(temp, x, y)
    dfs(depth+1, temp, dump)

  elif office[x][y] == 3:
    temp = copy.deepcopy(map)
    up(temp, x, y)
    right(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    right(temp, x, y)
    down(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    down(temp, x, y)
    left(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    left(temp, x, y)
    up(temp, x, y)
    dfs(depth+1, temp, dump)

  elif office[x][y] == 4:
    temp = copy.deepcopy(map)
    left(temp, x, y)
    up(temp, x, y)
    right(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    up(temp, x, y)
    right(temp, x, y)
    down(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    right(temp, x, y)
    down(temp, x, y)
    left(temp, x, y)
    dfs(depth+1, temp, dump)

    temp = copy.deepcopy(map)
    down(temp, x, y)
    left(temp, x, y)
    up(temp, x, y)
    dfs(depth+1, temp, dump)
  
  elif office[x][y] == 5:
    temp = copy.deepcopy(map)
    up(temp, x, y)
    down(temp, x, y)
    left(temp, x, y)
    right(temp, x, y)
    dfs(depth+1, temp, dump)
      
for i in range(M):
  for j in range(N):
    if office[i][j] != 0 and office[i][j] != 6:
      cctv.append([i, j])

dfs(0, office, cctv)
print(min_val)
