N = int(input())
foods = [list(map(str, input().split())) for _ in range(N)]

class Node:
    def __init__(self, foodName):
        self.foodName = foodName
        self.children = {} # 딕셔너리

class Tree:
    def __init__(self):
        self.root = Node(None)
        self.depth = 0

    def insertFoods(self, values):
        current_node = self.root

        for i in range(1, len(values)):
            if values[i] not in current_node.children:
                # 컬렉션['문자'] = 값  => '문자'는 key값.
                current_node.children[values[i]] = Node(values[i])

            current_node = current_node.children[values[i]]

        
    def traversal(self, node, depth):
        for child in sorted(node.children):
            floor = ''
            for _ in range(depth):
                floor += '--'
            
            print(floor + child)
            self.traversal(node.children[child], depth + 1) 

tree = Tree()

for f in foods:
    tree.insertFoods(f)

tree.traversal(tree.root, 0)