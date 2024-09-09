"""
퇴사2
https://www.acmicpc.net/problem/15486

N=퇴사날짜까지 남은 날
N+1=퇴사날
T=상담하는데 걸리는 일수
P=금액
하루에 할 수 있는 상담은 하나

정답=얻을 수 있는 최대 수익

7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

45
"""
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]

print(dp)

