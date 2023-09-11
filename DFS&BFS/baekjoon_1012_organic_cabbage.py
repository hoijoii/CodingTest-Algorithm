"""
유기농 배추
https://www.acmicpc.net/problem/1012

테스트케이스에 필요한 최소의 배추흰지렁이 수 print
bfs문제
"""
import sys
sys.setrecursionlimit(10**6)

T = int(input())

def bfs(x, y):
    #상하좌우
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for dir in direction:
       ny = y + dir[0]
       nx = x + dir[1]
       if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 1:
           graph[ny][nx] = 0
           bfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = [list(map(int, input().split())) for _ in range(K)] 
    graph = [[0 for _ in range(M)] for _ in range(N)]
    count = 0

    for X, Y in cabbages:
        graph[Y][X] = 1
    
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if graph[r][c] == 1:
                bfs(c, r)
                count += 1

    print(count)