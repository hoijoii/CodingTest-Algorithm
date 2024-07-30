"""
백스페이스: -
왼: < 오: >
"""

import sys

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = self.tail.next

  def insert(self, idx, value):
    current = self.head
    new_node = Node(value)

    # 맨 앞 insert
    if (idx==0):
      self.head = new_node
      new_node.next = current
    
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

N=int(input())
passwords = [sys.stdin.readline().strip() for _ in range(N)]

for string in passwords:
  linked_list = LinkedList()
  cursor = 0

  for key in string:
    if(key == '<' and cursor > 0):
      cursor -= 1
    elif(key == '>' and cursor < linked_list.get_length()):
      cursor += 1
    elif(key == '-' and cursor > 0):
      linked_list.delete(cursor)
      cursor -= 1
    elif(key.isalpha() or key.isdigit()):
      if(cursor == linked_list.get_length()):
        linked_list.append(key)
      else:
        linked_list.insert(cursor, key)
      cursor+=1
    
  print(linked_list.get_all())
    