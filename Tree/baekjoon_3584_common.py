"""
가장 가까운 공통 조상
https://www.acmicpc.net/problem/3584


두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은 노드.

"""

class Node:
  def __init__(self, num):
    self.num = num # 노드 넘버
    self.parent = -1 # 자기 부모
    self.children = [] # 자식이 여러 개

  def add_child(self, child):
    self.children.append(child)

  def add_parent(self, parent):
    self.parent = parent

def traversal(node):
  array = []
  if (node.parent != -1):
    array.append(node.parent)  
    traversal
  

T = int(input())

for _ in range(T):
  N = int(input())
  nodes_info = [list(map(int, input().split())) for _ in range(N-1)] # 앞에 거가 부모, 뒤에 거가 자식
  curious = map(int, input().split())

  tree = { i: Node(i) for i in range(1, N+1) }
  
  for p, c in nodes_info:
    tree[p].add_child(tree[c].num)
    tree[c].add_parent(tree[p].num)

  ancestors_1 = traversal(curious[0])
  ancestors_2 = traversal(curious[1])



# 노드 = 직원
class Node:
  def __init__(self, num):
    self.num = num # 사번
    self.compli_num = 0 # 받은 칭찬 수치
    self.children = [] # 여러 부하를 둘 수 있음

  def add_child(self, child):
    self.children.append(child)

  def add_compliment(self, num):
    self.compli_num += num

# 전위 순회
def preorder(node, parent_compli):
  if node:
    node.add_compliment(parent_compli) # 노드 자신의 칭찬 수치에 부모 칭찬수치를 더함

    if node.children:
      for child in node.children:
        preorder(tree[child.num], node.compli_num)

# 트리 만들기
tree = { i: Node(i) for i in range(1, N+1) }
root = tree[1]

# 자식 노드 추가
# idx+1 = 사번
for idx, boss in enumerate(boss_list):
  if(boss == -1): 
    continue
  tree[boss].add_child(tree[idx+1])

# 직속 상사에게 받은 칭찬 수치 더함
for num, comp in compliment:
  tree[num].compli_num += comp

preorder(root, 0) # 순회하며 칭찬 수치 더하기

for node in tree.values():
  print(node.compli_num, end=' ')

print('\n')