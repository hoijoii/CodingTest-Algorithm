"""
회사 문화 1
https://www.acmicpc.net/problem/14267


칭찬 수치만큼 부하들한테도 똑같이 칭찬함
1번 직원부터 n번 직원까지 칭찬 받은 정도 출력

입력: 
5 3
-1 1 2 3 4
2 2
3 4
5 6

출력:
0 2 6 6 12
"""
N, M = map(int, input().split()) # 회사 직원 수(직원은 1~N번 매겨져 있음), 최초의 칭찬 수
boss_list = list(map(int, input().split())) # 직원들 각각의 상사
compliment = [list(map(int, input().split())) for _ in range(M)] # 칭찬받은 직원의 칭찬 수치

# 한 노드 = 직원
class Node:
  def __init__(self, num, compli_num):
    self.num = num # 사번
    self.compli_num = compli_num # 받은 칭찬 수치
    self.children = [] # 여러 부하를 둘 수 있음

  def add_child(self, child):
    self.children.append(child)

# 전위 순회
def preorder(node, parent_compli):
  if node:
    node.compli_num += parent_compli # 노드 자신의 칭찬 수치에 부모 칭찬수치를 더함

    if node.children:
      for child in node.children:
        preorder(tree[child], node.compli_num)

# 노드 먼저 만들기
tree = { i: Node(i, 0) for i in range(1, N+1) }
root = tree[1]

# 자식 노드 추가
for child, boss in enumerate(boss_list):
  if(boss == -1): continue
  tree[boss].add_child(tree[child])

# 직속 상사에게 받은 칭찬 수치 저장
for num, comp in compliment:
  tree[num].compliment = comp

preorder(root, 0) # 순회하며 칭찬 수치 더하기

for num, node in tree.items():
  print(node.compli_num)