N = int(input())
lst = [list(map(str, input().split())) for _ in range(N)]

moment = [[int(team), list(map(int, time.split(':')))] for team, time in lst]

score_cnt = { 1: 0, 2: 0 }
win_time = { 1: [0,0], 2: [0,0] }

def calTime(pre, now):
  if pre[1] > now[1]:
    return [now[0]-pre[0]-1, now[1]+60-pre[1]]
  else:
    return [n-p for n, p in zip(now, pre)]

winning = [0, []] # 이기고 있는 팀, 득점시간
for i, [team, time] in enumerate(moment):
  score_cnt[team] += 1
  higher = [t for t, s in score_cnt.items() if max(score_cnt.values()) == s] # 최대값인 key 반환 [1], 최대값이 2개 이상이면 [1, 2]

  if len(higher) < 2: # 둘 중 하나가 이기고 있음
    wteam = higher[0]
    winning = [wteam, win_time[wteam]]
    if wteam == moment[i-1][0]: 
      continue

    if i==N-1: # 마지막 득점에서 안 비긴 경우
      win_time[winning[0]] = [i + j for i, j in zip(win_time[winning[0]], calTime(winning[1], [48, 0]))]
  
  else: # 비겼을 때 win_time을 갱신
    # 마지막 득점에서 비긴 경우 고려  
    win_time[winning[0]] = [i + j for i, j in zip(win_time[winning[0]], calTime(winning[1], time if i < N-1 else [48, 0]))]
    winning = [0, []]

for k, v in win_time.items():
  m = str(v[0]) if len(str(v[0])) > 1 else '0'+str(v[0])
  s = str(v[1]) if len(str(v[1])) > 1 else '0'+str(v[1])
  print(m+':'+s)