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
direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def one(i, j):
  for d in direction:
    if d[0] == 1 or d[0] == -1:
      for n in range(N):
        r, c = i+d[0], j+d[1]
        if n == N-1 and office[r][c] == 6: break

        


    
    

for i in range(M):
  for j in range(N):
    #cctv = office[i][j]
    #if office[i][j] != 0 and office[i][j] != 6: # cctv
    if office[i][j] == 1:
      one(i, j)
    elif office[i][j] == 2:
      


""" cctv = {1: [[[1,0]], [[-1,0]], [[0,-1]], [[0,1]]], #상하좌우
        2: [[[1,0], [-1, 0]], [[0,1], [0,-1]]], #상하, 좌우
        3: [[[1,0], [0,1]], [[0,1], [-1,0]], [[-1,0], [0,-1]], [[0,-1], [1, 0]]], #위오, 오아, 아왼, 왼위
        4: [[[0,-1], [1,0], [0,1]], [[1,0], [0,1], [-1,0]], [[0,1], [-1,0], [0,-1]], [[-1,0], [0,-1], [1,0]]], #왼위오, 위오아, 오아왼, 아왼위
        5: [[[1,0], [-1,0], [0,-1], [0,1]]] #모든방향
        }

def check(i, j):
  count = 0
  max_monitor = 0
  monitored = copy.deepcopy(office)
  r, c = i, j
  for direction in cctv[office[i][j]]:
    for d in direction:
      r,c = r+d[0], c+d[1]
      
      if (r == M-1 and (d[0]==1 or d[0]==-1)) or (c == N-1 and (d[1]==1 or d[1]==-1)) or office[r][c] == 6:
        break

      if office[r][c] == 0:
        monitored[r][c] = -1
        count += 1


for i in range(M):
  for j in range(N):
    #cctv = office[i][j]
    if office[i][j] != 0 and office[i][j] != 6: # cctv면
      check(i, j) """