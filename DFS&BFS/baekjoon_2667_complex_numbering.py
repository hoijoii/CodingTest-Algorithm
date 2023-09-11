"""
단지번호붙이기
https://www.acmicpc.net/problem/2667

bfs
단지 몇 개인지 찾기: bfs 다 돌면 count 하나 올리기

한 단지에 집 몇 개인지 찾기:
원래 위치인 x, y는 count 안 하고 nx, ny만 count하여 (nx, ny) 위치를 0으로 만듦
-문제점-
한 단지에 집이 여러 개일 때: bfs니까 여전히 1로 되어 있는 원래위치로 다시 돌아와서 count -> 집의 수에 영향 x
한 단지에 집이 한 개일 때: 원래 위치를 count 안 함, (nx, ny)가 없음 -> count를 아무것도 안하니까 0됨 -> 집의 수가 한 개인데 0임
=> bfs 재귀가 돌기 전에 원래 위치인 (x, y)가 1이면 count하기. 집이 여러개라도 어차피 nx, ny를 미리 0으로 처리하기 때문에 저 분기는 처음 한 번밖에 안 걸림
"""

N = int(input())
graph = [list(map(int, ''.join(input().split()))) for _ in range(N)]
count = 0
houses = 0
complexes = []

def bfs(x, y):
    global houses

    # 한 단지에 집이 한 채일 때 고려
    # 맨 처음 위치도 0으로 만들고 houses 카운트
    if graph[y][x] != 0:
        graph[y][x] = 0
        houses+=1

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dir in direction:
        ny = y+dir[0]
        nx = x+dir[1]

        if 0 <= ny < len(graph) and 0 <= nx < len(graph[0]) and graph[ny][nx] != 0:
            graph[ny][nx] = 0
            houses += 1
            bfs(nx, ny)

for r in range(len(graph)):
    for c in range(len(graph[0])):
        if graph[r][c] == 1:
            bfs(c, r)
            count += 1
            complexes.append(houses)
            houses=0

print(count)
for i in sorted(complexes):
    print(i)
