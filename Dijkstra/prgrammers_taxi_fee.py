"""
합승택시요금
https://school.programmers.co.kr/learn/courses/30/lessons/72413

4번에서 출발
n: 지점갯수
s: 출발
a: a집
b: b집
fares: [c, d, f] c와 d 사이의 택시요금이 f원
result:최저택시요금
"""
import heapq

def findCheapest(current, des, graph, n):
    # 현재장소랑 목적지 같으면
    if current == des:
        return 0
    # 연결된 다른 노드가 없으면
    if len(graph[des]) == 0:
        return float('inf')

    costs = [float('inf') for _ in range(n+1)]
    hq = []
    for next_pos, cost in graph[current]:
        heapq.heappush(hq, (cost, next_pos))
        costs[next_pos] = cost
    
    while hq:
        cost, pos = heapq.heappop(hq)
        if cost > costs[pos]:
            continue
        for next_pos, next_cost in graph[pos]:
            if costs[next_pos] > costs[pos] + next_cost:
                costs[next_pos] = costs[pos] + next_cost
                heapq.heappush(hq, (cost+next_cost, next_pos))
    
    return costs[des]
    

def solution(n, s, a, b, fares):
    fares = sorted(fares, key=lambda x: [x[0]])
    answer = float('inf')
    graph = [[] for _ in range(n+1)]

    for c, d, f in fares:
        if len(graph[c]) > 0:
            if graph[c][-1][1] == d:
                continue
        # 각각 노드에 (도착지, 코스트) 추가
        graph[c].append((d, f))
        graph[d].append((c, f))

    for i in range(1, n+1):
        cost = findCheapest(s, i, graph, n) + findCheapest(i, a, graph, n) + findCheapest(i, b, graph, n)
        if cost < answer:
            answer = cost

    return answer

