"""
2048
https://www.acmicpc.net/problem/12100

5번 움직여서 만들 수 있는 가장 큰 숫자 print

상하좌우
상[-1, 0] 하[1,0] 좌[0,-1] 우[0, 1]

짝수 갯수씩만 합쳐짐
같은 숫자일 때만 합쳐짐

dfs??? depth를 5까지로 .. ?

움직일 수 있는 경우
0 < ny < N
0 < nx < N

움직이는 모든 경우 고려
- 이동하는 방향에 블록이 있고 합쳐지는 경우:if(game[y][x]==game[ny][nx]) => game[ny][nx]=game[y][x]*2, game[y][x]=0
- 이동하는 방향에 블록이 있고 합쳐지지 않는 경우: game[ny][nx]
- 이동하는 방향에 블록이 없는 경우
"""

N = int(input())
init_game = [list(map(int, input().split())) for _ in range(N)]
maximum = 0

# 위에서 아래로 검사(열부터 검사)
def up(game):
    nxt_game = [[0 for _ in range(N)] for _ in range(N)]
    for c in range(N):
        point = -1 #기준 블럭

        for r in range(N):
            if game[r][c] != 0:
                if point == -1:
                    point = game[r][c]
                else:
                    if point == game[r][c]:
                        nxt_game[]
                

def dfs(game, depth):
    global maximum

    if depth == 5:
        for r in range(N):
            for c in range(N):
                maximum = max(maximum, game[r][c])
        return
    






