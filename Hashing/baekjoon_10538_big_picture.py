"""
10538: 빅 픽쳐

그림을 꿰매 이어붙여서 새로운 큰 그림을 만듦
큰 그림 중 어느 곳에 특정 그림이 사용되었는지 알아야 함.

그림은 x, o로 이루어짐
작은 그림 높이 너비 hp, wp
큰 그림 높이 너비 hm, wm

딕셔너리로 풀기??
큰 그림은 한 줄씩 그냥 문자열로 냅두고
작은 그림을 큰 그림에 한 줄씩 비교 (포함되어 있는지)
만약 한 줄 비교했을 때 포함되어 있는 것 같으면 flag값을 변경
flag값이 true면 다음 줄도 비교?
근디 .. 겹치는 구간이 있으면 어캄 ?? ㅜ
아예 ,,, 한 줄마다 패턴 똑같은 것 전부 다 검사?

"""
import sys 

width = list(map(int, input().split())) # [작은거h, 작은거w, 큰거h, 큰거w]

spic = [sys.stdin.readline().strip() for _ in range(width[0])] # 작은 그림
bpic = [sys.stdin.readline().strip() for _ in range(width[2])] # 큰 그림

# x:열 , y:행
def checkPic(x, y):
  for i in range(1, width[0]):
    bpic[y+i][x]