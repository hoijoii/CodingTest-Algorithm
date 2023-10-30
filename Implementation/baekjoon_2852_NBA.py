"""
NBA 농구
https://www.acmicpc.net/problem/2852

다른 팀을 역전할 때는 반드시 동점을 거쳐감. 
=> 동점일 때 or 마지막 득점일 때 계산

기록해야 하는 것!
이기고 있는 팀, 이기기 시작한 득점 시간 => 동점 or 마지막 득점일 때, 기록된 시간을 빼기만 하면 되니까 편함
"""
N = int(input())
lst = [list(map(str, input().split())) for _ in range(N)]

moment = [[int(team), list(map(int, time.split(':')))] for team, time in lst]

score_cnt = { 1: 0, 2: 0 }
win_time = { 1: [0,0], 2: [0,0] }

def minusTime(time1, time2):
  if time1[1] > time2[1]:
    return [time2[0]-time1[0]-1, time2[1]+60-time1[1]]
  return [n-p for n, p in zip(time2, time1)]
  
def plusTime(time1, time2):
  if time1[1]+time2[1] >= 60:
    return [time1[0]+time2[0]+1, time1[1]+time2[1]-60]
  return [time1[0]+time2[0], time1[1]+time2[1]]

winning = [0, []] # 지금 이기고 있는 팀, 이기기 시작한 득점시간
for i, [team, time] in enumerate(moment):
  score_cnt[team] += 1

  wteam = [t for t, s in score_cnt.items() if max(score_cnt.values()) == s] # 최대값인 key 반환 [1], 최대값이 2개 이상이면 [1, 2]
  if len(wteam) < 2: # 어느 한 팀이 이기고 있음
    if len(winning[1])==0: # 완전 처음 득점일 때 & 동점 후 처음 득점일 때
      winning = [wteam[0], time]

    if i == N-1: # 마지막 득점일 때
      win_time[winning[0]] = plusTime(win_time[winning[0]], minusTime(winning[1], [48, 0]))
  else: # 비김
    win_time[winning[0]] = plusTime(win_time[winning[0]], minusTime(winning[1], time))
    winning = [0, []]

for k, v in win_time.items():
  m = str(v[0]) if len(str(v[0])) > 1 else '0'+str(v[0])
  s = str(v[1]) if len(str(v[1])) > 1 else '0'+str(v[1])
  print(m+':'+s)