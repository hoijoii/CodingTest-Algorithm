"""
https://www.acmicpc.net/problem/2178

(1,1) ~ (N,M) => (0,0)~(N-1, M-1)
1은 이동, 0은 이동 x
카운트는 첫 번째 칸, 도착 칸 포함해서 셈.
bfs로 풀기. dfs로 풀려면 분기 끝까지 갔다가 돌아와야 하니까 오래걸림.
"""
n, m = map(int, input().split())
maze = [list(map(int, ''.join(input().split()))) for _ in range(n)]

visited = [[0 for j in range(m)] for i in range(n)]

#상하좌우
direction = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

def isMovable(maze, visited, nextPos):
    y = nextPos[0]
    x = nextPos[1]
    # 갈 위치가 미로의 범위를 벗어나는지
    if y < 0 or y > n-1 or x < 0 or x > m-1:
        return False   
    # 갈 위치가 벽이거나 방문했던 곳인지
    if maze[y][x] == 0 or visited[y][x] > 0:
        return False
    return True

# bfs
def findPath(maze, visited):
    queue = [[0,0]] # 시작지점
    visited[0][0] = 1 # 시작지점
    x = 0
    y = 0
    nx = 0
    ny = 0
    
    while len(queue) > 0:
        y, x = queue.pop(0)
        
        # 도착지점에 도착하면 끝
        if [y, x] == [n-1, m-1]:
            return visited[y][x]
        
        for i in range(4):
            ny = y + direction[i][0]
            nx = x + direction[i][1]

            if isMovable(maze, visited, [ny, nx]):
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

print(findPath(maze, visited))