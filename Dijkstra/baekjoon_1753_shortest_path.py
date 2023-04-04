import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
start = int(input())

inf = float('inf')
graph = [[] for _ in range(V+1)]
distance = [inf] * (V+1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((b, c))

#dijkstra
def shortest_path(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start]

    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue

        for i in graph[now]:
            cost = dis + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

shortest_path(start)

for i in range(1, V+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])






""" import heapq

ve = list(map(int, input().split())) # V, E
start = int(input())
uvw = [list(map(int, input().split())) for _ in range(ve[1])] # u, v, w

# 비용테이블 만들기
costs = [[float('inf') for _ in range(ve[0])] for _ in range(ve[0])] # 비용 테이블 (행:출발노드, 열:도착노드, 값:비용)

for r in range(ve[0]):
    costs[r][0] = 0

for u, v, w in uvw:
    costs[u-1][v-1] = w

print(costs)

# priority queue 힙 구조 dijkstra

def dijkstra(graph, starting):
    distances = {str(vertex+1): float('inf') for vertex in range(len(ve[0]))} # 최소비용 테이블
    distances[starting] = 0 #starting vertex의 cost는 0

    pq = [(0, starting)] # priority queue, 탐색할 노드 보관

    # pq 안에 값이 사라질 때까지 반복
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq) #pop된 노드가 (distance, vertex) 형식 .
        
        #
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
    

dijkstra(costs, start)
 """