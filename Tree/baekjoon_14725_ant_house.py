"""
로봇개미
각 층에 먹이가 있는 방을 따라가다가 더이상 내려갈 수 없으면 안움직이고 그 자리에서 신호보냄

내려오면서 알게 된 먹이 정보들을 제공

개미들이 보내준 정보
KIWI BANANA
KIWI APPLE
APPLE APPLE
APPLE BANANA KIWI

input: 
먹이 정보 개수 (N)
두번째 줄부터 N+1 번째 줄까지 먹이 정보 개수 K, K 옆에는 K개의 먹이 이름 써줌

output:
각 층을 --로 구분, 같은 층에 여러 개 방이 있을 때 사전순서가 앞서는 먹이 정보 먼저 나옴
A
--B
----C
------D
--C
B
--A

시각화되어 출력되게끔 하기

결국 탐색 문제 아닝교 ??

root: 개미굴입구
dfs 사용?
"""

N = int(input())
foods = [list(map(str, input().split())) for _ in range(N)]

class Node:
    def __init__(self, foodName):
        self.foodName = foodName
        self.children = {} # 딕셔너리 자료형

class Tree:
    def __init__(self):
        self.root = Node(None)

    def insertFoods(self, values):
        current_node = self.root

        for i in range(1, len(values)):
            if values[i] not in current_node.children:
                # 컬렉션['문자'] = 값  => '문자'는 key값.
                current_node.children[values[i]] = Node(values[i])

            current_node = current_node.children[values[i]]


tree = Tree()

for f in foods:
    tree.insertFoods(f)