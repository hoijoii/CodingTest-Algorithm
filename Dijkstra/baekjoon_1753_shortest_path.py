import heapq

ve = list(map(int, input().split())) # V, E
start = int(input())
uvw = [list(map(int, input().split())) for _ in range(ve[1])] # u, v, w

""" costs = [[INF for _ in range(ve[0])] for _ in range(ve[0])] # 비용 테이블 (행:출발노드, 열:도착노드, 값:비용)
for u, v, w in uvw:
    costs[u-1][v-1] = w """

"""priority queue 힙 구조 사용할 것"""

def dijkstra(graph, starting):
    distances = {vertex: float('inf') for vertex in graph}
    distances[starting] = 0 #starting vertex의 cost는 0

    pq = [(0, starting)] # priority queue, 탐색할 노드 보관

    # pq 안에 값이 사라질 때까지 반복
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq) #pop된 노드가 (distance, vertex) 형식 .
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
    
graph = {}

for i in range(ve[0]):
    graph[str(i+1)]