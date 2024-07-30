"""
백준 2164: 카드2

1~N까지 번호 붙어있음. 1이 제일 위
카드가 한 장 남을 때까지 반복할 것:
제일 위 카드를 버림 -> 그 다음 카드를 제일 아래 카드 밑으로 옮김
제일 마지막 카드 print
입력:6 -> 출력:4
"""
from collections import deque

N = int(input())
cards = deque(range(1, N + 1))

while(len(cards)>1):
  cards.popleft() # 맨 윗장을 바닥에 버림
  cards.append(cards.popleft()) # 그 다음 맨 윗장을 맨 아래에 옮김

print(cards[0])