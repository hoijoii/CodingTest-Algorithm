"""
공주님의 정원
https://www.acmicpc.net/problem/2457

이중 for문은 시간복잡도 n^2으로 실패 ..

고려할 것:
1. 지금 꽃의 피는 날이 이전에 심은 꽃의 지는 날 이전 or 같은 날인가
2. 위 조건에 해당하는 꽃들의 지는 날짜가 가장 마지막인 꽃 고르기

처음엔 꽃피는 날에 따라 조건 달 거라서 피는 날 기준으로 정렬
while문으로 반복하면서 꽃 하나하나 검사
지금 꽃의 피는 날이 이전 꽃 지는 날 전이거나 같은 날이면 일단 temp에 담음
-> 반복문 돌다 보면 이 조건에 해당하지 않는 원소 나옴
그때 temp의 원소들을 지는 날 기준으로 정렬하면 temp[-1]이 가장 나중에 지는 꽃임.
temp[-1]을 garden에 담고 i는 플러스하지 않고 while문 continue해서 그 원소부터 검사함

"""
N = int(input())
periods = [list(map(int, input().split())) for _ in range(N)]
garden=[[1, 1, 3, 1]] # 꽃 골라담기 리스트

periods.sort(key=lambda x: [x[0], x[1]])

i = 0
temp = []
while(i < N):
  # 마지막 심은 꽃의 지는 날이 이미 12월일 경우
  if garden[-1][2] == 12:
    break
  
  # 지금 꽃의 피는 날이 이전 꽃의 지는 날 이전 or 같은 날인가
  if periods[i][0] < garden[-1][2] or (periods[i][0]==garden[-1][2] and periods[i][1] <= garden[-1][3]):
    temp.append(periods[i])
  # 위 조건에 해당하지 않는 꽃 등장하면 이제까지 temp에 모은 꽃 중 지는날 정렬
  else:
    if temp:
      temp.sort(key=lambda x: [x[2], x[3]])
      garden.append(temp[-1]) # 가장 나중에 지는 꽃 garden에 추가
      temp = []
      continue # 현재 원소부터 다시 검사
    else:
      garden=[[1, 1, 3, 1]] #초기화
      break

  # 마지막 원소까지 왔을 때 지는 날이 12월에 도달했는지 고려
  if i == N-1 and temp:
    temp.sort(key=lambda x:[x[2], x[3]])
    if temp[-1][2] == 12:  # 지는 날이 12월이면 꽃 고르기
      garden.append(temp[-1])
    else:                  # 아니면 꽃 고르기 실패 
      garden=[[1, 1, 3, 1]] #초기화  
      break

  i+=1

print(len(garden)-1)

""" 
--시간초과 오답--

for _ in range(len(periods)):
  temp = []
  for period in periods:
    # 이번 꽃 피는 날짜가 이전 꽃 지는 날의 '이전 월'이거나 '같은 월이면서 일자가 전'인 경우
    if period[0] < garden[-1][2] or (period[0] == garden[-1][2] and period[1] <= garden[-1][3]):
      temp.append(period) #일단 조건에 해당하는거 temp에 다 담음
  
  # 고려할 것.. temp에 들어있다는 건 피는 날짜가 범위에 잘 들어와 있다는 것임!! 지는 날이 가장 나중인 걸 선택해야 함.
  if temp:
    garden.append(sorted(temp, key=lambda x:[x[2], x[3]])[-1])
    
  else:
    garden = [[1, 1, 3, 1]] #초기화
    break
  
  if garden[-1][2] == 12: break
 """