"""
도서관
https://www.acmicpc.net/problem/1461

음수, 양수끼리 모아서 M개씩 
제일 먼 거 두개를 마지막에.

"""

N, M = map(int, input().split())
locations = list(map(int, input().split()))
locations.sort()

answer = 0
minus, plus = [], []

for l in locations:
  if l < 0: minus.append(l)
  else: plus.append(l)

for i in range(0, len(minus), M):
    answer += abs(minus[i]*2)

for i in range(len(plus)-1, -1, -M):
    answer += plus[i]*2

if plus and minus: answer -= max(abs(minus[0]), plus[len(plus)-1])
elif plus: answer -= plus[len(plus)-1]
elif minus: answer -= abs(minus[0])

print(answer)
