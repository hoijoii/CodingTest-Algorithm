"""
환상의 듀엣
https://www.acmicpc.net/problem/11570

차가 적은 값들을 묶어야 함 - 두묶음으로
어떻게~해야하나,,
전부 계산..?
정렬 후 차가 작은 것들끼리 묶기. 왜냐면 작은 수랑 큰 수는 항상 차가 크니까
"""
N = int(input())
music = list(map(int, input().split()))
diffs = []
answer = 0

music.sort()
print(music)
for i in range(len(music)-1):
  diffs.append(abs(music[i]-music[i+1]))

pivot = diffs.index(max(diffs))+1

for i in range(pivot-1):
  answer += abs(music[i]-music[i+1])
  print(abs(music[i]-music[i+1]))
  
print('----')

for i in range(pivot, len(music)-1):
  answer += abs(music[i]-music[i+1])
  print(abs(music[i]-music[i+1]))

print(answer)