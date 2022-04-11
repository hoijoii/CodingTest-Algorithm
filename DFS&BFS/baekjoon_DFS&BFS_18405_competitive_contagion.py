from collections import deque

# bfs로 바이러스 퍼뜨림
def virus(queue):
    while queue:
        v, x1, y1, t = queue.popleft() # v:바이러스 종류 / x1:좌표x / y1:좌표y / t:시간
        if t == s:
            break
        else:
            for i in dir:
                x2, y2 = i
                # 상하좌우로 퍼지는 조건
                if 0 <= x1 + x2 < n and 0 <= y1 + y2 < n and tube[x1+x2][y1+y2] == 0:
                    tube[x1+x2][y1+y2] = v
                    queue.append([v, x1 + x2, y1 + y2, t + 1])

n, k = map(int, input().split())
tube = [[int(x) for x in input().split()] for y in range(n)]
s, x, y = map(int, input().split())
list = []

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 방향 바꿈. 상하좌우

# 시험관 상태를 큐에 넣음
for i in range(n):
    for j in range(n):
        if tube[i][j] != 0:
            list.append([tube[i][j], i, j, 0])

list.sort() # 바이러스 오름차순
queue = deque(list)

virus(queue)
print(tube[x-1][y-1])