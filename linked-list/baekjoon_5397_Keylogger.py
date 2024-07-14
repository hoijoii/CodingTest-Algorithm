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

N=int(input())
passwords = [sys.stdin.readline().strip() for _ in range(N)]

linked_list = LinkedList()

for string in passwords:
  cursor = len(password)

  for key in string:
    if(key == '<'):
      if(cursor>0) 