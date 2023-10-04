"""
2048
https://www.acmicpc.net/problem/12100

최대 5번 움직일 수 있다는 조건 하에
1번 움직일 때마다 상하좌우 경우를 또 고려해야 하므로 dfs. 최대 depth를 5로 두기.

상하좌우 움직이는 함수를 각각 만듦. 방향마다 검사 방향이 다름.
예) 위쪽으로 블록을 이동시킬 때 위부터 검사해야 기준블럭과 같은 숫자를 찾아 합칠 수 있음.
상: 위->아래로 검사
하: 아래->위
좌: 왼->오
우: 오->왼


"""

N = int(input())
init_game = [list(map(int, input().split())) for _ in range(N)]
maximum = 0

# 위에서 아래로 검사(열부터 검사)
def up(game):
    nxt_game = [[0 for _ in range(N)] for _ in range(N)] #움직임 후 블록 기록할 리스트

    for c in range(N):
        point = -1 #기준 블럭
        row = 0 # 한 열에서 블록들이 이동되어 있는 행

        for r in range(N):
            # 블록이 있을 때
            if game[r][c] != 0:
                #기준 블럭이 없으면 기준 블럭으로 설정
                if point == -1:
                    point = game[r][c]
                else:
                    #기준블럭 값과 같으면
                    if point == game[r][c]:
                        nxt_game[row][c] = point * 2 # 다음 게임판에 저장하기
                        point = -1
                    else:
                        nxt_game[row][c] = point
                        point = game[r][c]
                    row += 1
        # 남은 블럭 기록
        if point != -1:
            nxt_game[row][c] = point

    return nxt_game

# 아래서 위로 검사
def down(game):
    nxt_game = [[0 for _ in range(N)] for _ in range(N)]
    
    for c in range(N):
        point = -1
        row = 0

        for r in range(N-1, -1, -1):
            if game[r][c] != 0:
                if point == -1:
                    point = game[r][c]
                else:
                    if point == game[r][c]:
                        nxt_game[row][c] = point * 2 
                        point = -1
                    else:
                        nxt_game[row][c] = point
                        point = game[r][c]
                    row += 1
        
        if point != -1:
            nxt_game[row][c] = point

    return nxt_game

# 왼->오 검사
def left(game):
    nxt_game = [[0 for _ in range(N)] for _ in range(N)]
    
    for r in range(N):
        point = -1
        col = 0   

        for c in range(N):
            if game[r][c] != 0:
                if point == -1:
                    point = game[r][c]
                else:
                    if point == game[r][c]:
                        nxt_game[r][col] = point * 2 
                        point = -1
                    else:
                        nxt_game[r][col] = point
                        point = game[r][c]
                    col += 1
        
        if point != -1:
            nxt_game[r][col] = point

    return nxt_game

# 오->왼 검사
def right(game):
    nxt_game = [[0 for _ in range(N)] for _ in range(N)]
    
    for r in range(N):
        point = -1
        col = 0

        for c in range(N-1, -1, -1):
            if game[r][c] != 0:
                if point == -1:
                    point = game[r][c]
                else:
                    if point == game[r][c]:
                        nxt_game[r][col] = point * 2 
                        point = -1
                    else:
                        nxt_game[r][col] = point
                        point = game[r][c]
                    col += 1
        
        if point != -1:
            nxt_game[r][col] = point

    return nxt_game
                
def dfs(game, depth):
    global maximum

    if depth == 5:
        #최대값찾기
        for r in range(N):
            for c in range(N):
                maximum = max(maximum, game[r][c])
        return

    else:
        dfs(up(game), depth+1)
        dfs(right(game), depth+1)
        dfs(down(game), depth+1)
        dfs(left(game), depth+1)

dfs(init_game, 0)
print(maximum)






