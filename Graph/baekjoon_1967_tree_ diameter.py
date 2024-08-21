"""
트리의 지름
https://www.acmicpc.net/problem/1967

트리인데 가중치가 있음 = 그래프
가중치=길이
트리의 지름=트리를 쫙 폈을 때 가장 긴 경로

dfs 이용..
1. 아무 노드에서부터 출발해 제일 먼 노드를 찾기 => dfs(1)
  - 이유: 트리의 가지마다 간선의 합이 다 정해져 있기 때문에, 어디서 출발하든 가중치가 큰 애들이 가장 먼 노드로 선택될 수밖에 없음.
  - 어떤 노드로부터 가장 먼 노드는 무조건 말단 노드임
2. 제일 먼 노드에서부터 또 제일 먼 노드를 찾기 => dfs(node)
  - 그래야 지름이 나오니까~
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())

if (N == 1): print(0)
else :
  graph = {}

  # 그래프 만들기
  for _ in range(N-1):
    [parent, child, weight] = list(map(int, input().split()))
    # graph에 키값이 없으면 parent: []로 생성하고 append, 있으면 바로 append
    graph.setdefault(parent, []).append([child, weight])
    graph.setdefault(child, []).append([parent, weight])

  def dfs(cur_v, visited, cur_sum):
    visited.add(cur_v)
    farthest_v = cur_v
    max_sum = cur_sum

    for v, w in graph[cur_v]:
      if v not in visited:
        node, distance = dfs(v, visited, cur_sum+w)
        if distance > max_sum:
          max_sum = distance
          farthest_v = node
    
    return farthest_v, max_sum

  farthest_A, distance_A = dfs(1, set(), 0) # 가장 끝에 있는 노드 중 하나(A), 거기까지의 거리
  farthest_B, distance_B = dfs(farthest_A, set(), 0) # A에서 가장 먼 노드 B, A에서 B까지의 거리

  print(distance_B)