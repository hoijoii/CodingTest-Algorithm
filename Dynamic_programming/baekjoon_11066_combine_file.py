"""
파일 합치기
https://www.acmicpc.net/problem/11066
https://seongmok.com/45

두 파일을 합친 비용들을 최종적으로 다 더해줘야함.
40 30 30 50
40+30=70
30+50=80
70+80=150
=> 70+80+150=300
풀어쓰면 (40+30)+(30+50)+((40+30)+(30+50))

(틀린답)
30+30=60
40+60=100
50+100=150
=>60+100+150=310
(30+30)+((30+30)+40)+(50+(30+30+40))=310

뒤의 괄호부분은 변하지 않는 값. 어떻게 더해도 결국 전체를 한 번 다 더한 값.
즉 앞에 두 괄호값이 최소가 되면 됨. 

dp[i][j]: i부터 j까지 합쳤을 때 최소 비용
dp[i][i]: 파일 i의 크기

dp[i][j]가 최소가 되는 pivot 찾기

"""

T = int(input()) # 테스트케이스 수

for _ in range(T):
  K = int(input()) # 장의 수
  costs = list(map(int, input().split())) # 장마다 코스트
  dp = [[0]*(K+1) for _ in range(K+1)]
  add = [0]*(K+1)

  for i in range(K):
    add[i+1] = add[i]+costs[i]
  
  # dp[r][c]가 최소가 되도록 pivot 이용(dp[r][c]: r부터 c까지 합쳤을 때 최소비용)
  for i in range(K):
    r=1
    c=i+1
    for _ in range(K-i):
      dp[r][c] = float('inf')
     
      for pivot in range(c-i, c):
        dp[r][c] = min(dp[r][c], dp[r][pivot]+dp[pivot+1][c]+add[c]-add[r-1])
        print(r, c, dp[r][pivot], dp[pivot][c], add[c], add[r-1])
      r+=1
      c+=1

print(dp[0][K])

""""
2
4
40 30 30 50
"""