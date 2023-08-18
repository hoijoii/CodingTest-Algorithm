"""
양방향 통행 도로
다익스트라
1 출발 노드 설정, 출발노드 기준으로 각 노드의 최소비용 저장
2 방문 안 한 노드 중 가장 비용이 적은 노드 선택
3 해당 노드 거쳐 목적지까지 가는 경우 고려해 최소비용 갱신
4 2, 3반복

N: 마을 수
road: 도로 정보. [마을1, 마을2, 시간]
K: 제한시간

1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.
딕셔너리 1번의 한 줄이 완성되면 .. 끝?

우선순위 큐 사용(heapq)

다시 이전 노드로 돌아가는 선택지는 없기 때문에 
그래프 리스트에 최초로 (a, b, cost)를 append하고 나서 (b, a, cost)를 또 append할 필요가 없다.
"""

import heapq

def dijkstra(graph, time):
    q = []
    heapq.heappush(q, (0, 0)) # 시간, 출발지 (우선순위, 값)
    time[0] = 0

    while q:
        t, current = heapq.heappop(q) # 가장 짧은 시간 pop (우선순위 값이 가장 작은 거)
        # time에 기록되어있던 시간이 현재까지의 시간보다 짧으면 갱신할 필요 없음.
        if time[current] < t:
            continue
        
        #연결된 모든 노드 탐색
        for b, b_time in graph[current]:
            # 현재까지의 시간 + 현재노드에서 b까지의 시간 < time에 기록되어 있던 b까지의 시간
            if t + b_time < time[b]:
                time[b] = t + b_time # 현재까지의 시간이 더 짧으니까 time을 갱신
                heapq.heappush(q, (t + b_time, b))


def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N)]
    time = [float('inf')] * N

    for a, b, cost in road:
        if a<=b: 
            # graph[출발지]=(도착지, 가중치)
            graph[a-1].append((b-1, cost)) 
        else: 
            # 작은 노드부터 검사할 건데 a가 b보다 크면([5,2,2]같은거) b번 노드를 검사할 때 a를 검사 안 함.
            # 그래서 graph[작은노드].append((큰 노드, 코스트))
            graph[b-1].append((a-1, cost))

    dijkstra(graph, time)
    for t in time:
        if t <= K:
            answer+=1
    return answer

solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
#4