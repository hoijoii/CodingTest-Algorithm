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
        current = current.next
      current.next = Node(value)
  
  def insert(self, idx, value):
    new_node = Node(value)
    current = self.head

    if(idx == 0):
      new_node.next = current
      self.head = new_node
      return
  
    for _ in range(idx-1):
      current = current.next
    new_node.next = current.next
    current.next = new_node
    return

  def delete(self, idx):
    current = self.head

    if(idx == 0):
      return

    if(idx == 1):
      self.head = current.next
      return

    else:
      for _ in range(idx-2): # 삭제될 노드의 앞 노드를 찾음 
        current = current.next
      
      if (current.next.next == None):
        current.next = None
        return

      current.next = current.next.next
      return

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
  if(command[0] == 'L'):
    if cursor==0:
      continue
    cursor -= 1
  elif(command[0] == 'D' and cursor<linked_list.get_length()):
    cursor += 1
  elif(command[0] == 'B'):
    if (cursor > 0):
      linked_list.delete(cursor)
      cursor -= 1
  elif(command[0] == 'P'):
    if cursor == linked_list.get_length(): 
      linked_list.append(command[1])
    else:
      linked_list.insert(cursor, command[1]) 
    cursor += 1

print(linked_list.get_all())