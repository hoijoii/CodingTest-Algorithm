"""
가장 가까운 공통 조상
https://www.acmicpc.net/problem/3584


두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은 노드.

"""
import sys
sys.setrecursionlimit(10**6)

class Node:
  def __init__(self, num):
    self.num = num # 노드 넘버
    self.parent = -1 # 부모
    self.children = [] # 자식이 여러 개

  def add_child(self, child):
    self.children.append(child)

  def set_parent(self, parent):
    self.parent = parent

def traversal(tree, node, array):
  array.append(node.num) # 자기 자신도 조상이 될 수 있으니까 append
  # 조상이 없으면 조상 array 리턴
  if node.parent == -1 :
    return array
  else:
    return traversal(tree, tree[node.parent], array)

T = int(input())

for _ in range(T):
  N = int(input())
  nodes_info = [list(map(int, input().split())) for _ in range(N-1)] # 앞에 거가 부모, 뒤에 거가 자식
  curious = list(map(int, input().split()))

  # 같은 노드면 자기 자신이 젤 가까움
  if(curious[0] == curious[1]) :
    print(curious[0])
    continue
  
  # 트리를 먼저 만듦
  tree = { i: Node(i) for i in range(1, N+1) }

  # 부모 자식 관계 설정
  for p, c in nodes_info:
    tree[p].add_child(tree[c].num)
    tree[c].set_parent(tree[p].num)
  
  ancestors_1 = []
  ancestors_2 = []

  # 공통조상 찾기
  traversal(tree, tree[curious[0]], ancestors_1)
  traversal(tree, tree[curious[1]], ancestors_2)

  # ancestors 배열들은 자기 자신부터 가장 먼 조상 순서로 채워져있음
  for a in ancestors_2:
    # 빠른 검색 위해 set() 사용
    if a in set(ancestors_1):
      print(a)
      break
