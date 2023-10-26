"""
NBA 농구
https://www.acmicpc.net/problem/2852

농구경기는 48분
입력: 팀번호 득점시간
각 팀이 몇 분 동안 이기고 있었는지 00:00 형식으로 출력
팀은 2개(1, 2)

몇대몇인지도 고려
동점일 때는 양쪽 다 카운트 x
점수가 높은 쪽이 생기면 그때부터 카운트해야함
다른 팀을 역전할 때는 반드시 동점인 순간이 있음.

pre 초기화해주면 48분 calculate 계산이 이상하게 됨.. 

기록해야 하는 것
이전에 득점한 팀
이기고 있는 팀, 그 팀의 이기고 있던 시간
"""

N = int(input())
lst = [list(map(str, input().split())) for _ in range(N)]

moment = [[int(team), list(map(int, time.split(':')))] for team, time in lst]
now_score = { 1: 0, 2: 0 }
win_time = { 1: [0, 0], 2: [0, 0] }

def calculate(pre, now):
  if pre[1] > now[1]:
    return [now[0]-pre[0]-1, now[1]+60-pre[1]]
  else:
    return [n-p for n, p in zip(now, pre)]

pre = [0, []] # 팀, 득점시간
for i, [team, time] in enumerate(moment):
  now_score[team] += 1

  winning = [t for t, s in now_score.items() if max(now_score.values()) == s] # 최대값인 key 반환 [1], 최대값이 2개 이상이면 [1, 2]
  print(winning)
  if len(winning) < 2:  # 둘 중 하나가 이기고 있음
    if pre[0] or (win_time[1] or win_time[2]):
      if pre[0] == winning[0]: # 이전 득점한 팀이 이기고 있으면
        print('pre :: ', pre)
        continue
      else: # 다른 팀이 득점
        pre = [winning[0], time]

      if i == N-1: 
        print('last')
        win_time[winning[0]] = [i + j for i, j in zip(win_time[winning[0]], calculate(pre[1], [48, 0]))]
    else:
      pre = [team, time]

    """ elif not pre[0]:
      pre = [winning[0], time] """

  else: # 비김
    win_time[pre[0]] = [i + j for i, j in zip(win_time[pre[0]], calculate(pre[1], time))] #지금까지 득점하고 있던 팀 시간 끝내기
    pre = [0, []]

    #pre = [team, time]
  print('win time:: ', win_time)
  print('pre :: ', pre)

for k, v in win_time.items():
  m = str(v[0]) if len(str(v[0])) > 1 else '0'+str(v[0])
  s = str(v[1]) if len(str(v[1])) > 1 else '0'+str(v[1])
  print(m+':'+s)