"""
환상의 듀엣
https://www.acmicpc.net/problem/11570

차가 적은 값들을 묶어야 함 - 두묶음으로
어떻게~해야하나,,
전부 계산..?
정렬 후 차가 작은 것들끼리 묶기. 왜냐면 작은 수랑 큰 수는 항상 차가 크니까

노래를 부를 때 음의 순서가 바뀌면 안 됨 .. => 정렬 x
pivot을 정하고 그거보다 큰 숫자들은 차례로 연산?

정렬해서 pivot 찾고 music에서 해당하는 원소들 차례로 연산

상덕이는 작은거부터
희원이는 큰거부터 계산?
"""
N = int(input())
music = list(map(int, input().split()))

diffs = []
sang, hee = [], []
answer = 0

for i in range(len(music)):
  if abs(max(music)-music[i]) > abs(min(music)-music[i]):
    sang.append(music[i])
  elif abs(max(music)-music[i]) < abs(min(music)-music[i]):
    hee.append(music[i])  

for i in range(len(sang)-1):
  answer += abs(sang[i]-sang[i+1])

for i in range(len(hee)-1):
  answer += abs(hee[i]-hee[i+1])

print(answer)

""" sorted_music = sorted(music)

for i in range(len(music)-1):
  #print(abs(sorted_music[i]-sorted_music[i+1]))
  diffs.append(abs(sorted_music[i]-sorted_music[i+1]))

pivot = sorted_music[diffs.index(max(diffs))+1]

for i in range(len(music)):
  if music[i] < pivot:
    sang.append(music[i])
  else:
    hee.append(music[i])

for i in range(len(sang)-1):
  answer += abs(sang[i]-sang[i+1])

for i in range(len(hee)-1):
  answer += abs(hee[i]-hee[i+1])

print(answer) """

""" music.sort()
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

print(answer) """