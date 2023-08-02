"""
미로탈출
https://school.programmers.co.kr/learn/courses/30/lessons/159993

레버까지 가는 최단거리 시간 + 레버에서 출구까지의 최단거리 시간
경로가 겹쳐도 되니까
findPath함수: 시작점->도착점 최단시간 구하는 함수
findPath함수를 두번 실행시켜서 sl, le에 각각의 최단시간 저장

S -> L 도착하면 카운트(visited) 초기화
L -> E 에서 다시 첨부터 카운트
그리고 둘을 더함

만약 도착 못하면 None반환
sl이랑 le 둘 중 하나라도 None이면 return -1

"""
from collections import deque

def isMovable(maps, visited, nextPos, start):
    y = nextPos[0]
    x = nextPos[1]
    # 갈 위치가 미로의 범위를 벗어나는지
    if y < 0 or y > len(maps)-1 or x < 0 or x > len(maps[0])-1:
        return 
    # 갈 위치가 'S'이면서 벽이거나 방문했던 곳인지
    if [y, x] == start or maps[y][x] == 'X' or visited[y][x] > 0:
        return 
    
    return True

#bfs
def findPath(maps, milestone, start, end):
    ny, nx = 0, 0
    deq = deque([milestone[start]])
    visited = [[0 for j in range(len(maps[0]))] for i in range(len(maps))]
    #상하좌우
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while len(deq) > 0:
        y, x = deq.popleft() # 시작지점

        # 도착
        if [y, x] == milestone[end]:
            return visited[y][x]
    
        for i in range(4):
            ny = y + direction[i][0]
            nx = x + direction[i][1]

            if isMovable(maps, visited, [ny, nx], milestone[start]):
                visited[ny][nx] = visited[y][x] + 1
                deq.append([ny, nx])
        
def solution(maps):
    answer = 0
    milestone = {'S': [], 'L': [], 'E':[]}

    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                milestone['S'] = [r, c]
            if maps[r][c] == 'L':
                milestone['L'] = [r, c]
            if maps[r][c] == 'E':
                milestone['E'] = [r, c]
        if milestone['S'] and milestone['L'] and milestone['E']:
            break
    
    # 파라미터: maps, SLE좌표, 시작점, 끝점
    sl = findPath(maps, milestone, 'S', 'L')
    le = findPath(maps, milestone, 'L', 'E')

    if sl == None or le == None:
        answer = -1
    else: 
        answer = sl + le

    return answer
