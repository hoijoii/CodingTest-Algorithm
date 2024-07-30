"""
L: 왼
D: 오
B: 왼쪽 문자 삭제
P$: 왼쪽에 문자 넣음($)
"""
import sys

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, value):
    if not self.head:
      self.head = Node(value)
    else:
      current = self.head
      while current.next:
        current=current.next
      current.next = Node(value)

  def insert(self, idx, value):
    current = self.head
    new_node = Node(value)

    # 맨 앞 insert
    if (idx==0):
      self.head = new_node
      new_node.next = current
    
    # 중간에서 insert
    else:
      for _ in range(idx-1):
        current = current.next # insert할 곳 직전 노드 찾기
      new_node.next = current.next
      current.next = new_node

  def delete(self, idx):
    current = self.head

    # 한 글자일 때
    if(current.next == None):
      self.head=None
      return

    # 두 글자 이상일 때
    for _ in range(idx-2):
      current = current.next
    
    if(current.next.next):
      current.next = current.next.next
    else:
      current.next = None

  def get_length(self):
    current = self.head
    length = 0
    while current:
      current = current.next
      length += 1
    return length
  
  def get_all(self):
    current = self.head
    result = ''
    while current:
      result += current.value
      current = current.next
    return result

string = sys.stdin.readline().strip()
M=int(input())
edit=[list(map(str, input().split())) for _ in range(M)]

linked_list = LinkedList()
cursor = len(string)# 커서 위치(0은 첫 글자 앞, len(stirng)은 맨 끝 글자 뒤)

# 초기화
for val in string:
  linked_list.append(val)

for command in edit:
  if(command[0] == 'L' and cursor > 0):
    cursor -= 1
  elif(command[0] == 'D' and cursor < linked_list.get_length()):
    cursor += 1
  elif(command[0] == 'B' and cursor > 0):
    linked_list.delete(cursor)
    cursor -= 1
  elif(command[0] == 'P'):
    if cursor == linked_list.get_length(): 
      linked_list.append(command[1])
    else:
      linked_list.insert(cursor, command[1]) 
    cursor += 1

print(linked_list.get_all())