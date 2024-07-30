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

트라이?
kmp?
라빈카프?
롤링해시?

근디.. 그러면 반복문 돌면서 계속 해시함수를 적용해야 하는데

"""
import sys 

width = list(map(int, input().split())) 
[sh, sw, bh, bw] = width # [작은거h, 작은거w, 큰거h, 큰거w]

spic = [sys.stdin.readline().strip() for _ in range(sh)] # 작은 그림
bpic = [sys.stdin.readline().strip() for _ in range(bh)] # 큰 그림
cnt = 0 # 답(영역 개수)

d = 256 # 집합의 크기(ASCII 코드) - 문자 위치의 영향을 반영하기 위한 변수
q = 103 # 해싱에 자주 쓰이는 소수 (101,, 307 ,, 암거나 적당한 수)

# 라빈 핑거프린트 해싱
def hashing(string, idx):
  value = 0

  if (idx is None):
    for i, s in enumerate(string):
      value += ord(s) * (d**(sw-(i+1)))
    value = value % q
  else:
    value = ord(string) * (d**(sw-1)) % q if(idx==-1) else ord(string)
  
  return value

""" def hashing(string, idx):
  value=0

  if(idx is None):
    for i, s in enumerate(string):
      value += ord(s)*(2**(sw-(i+1))) # 공식
  
  else:
    value = ord(string)*(2**(sw-1)) if (idx==-1) else ord(string)

  return value """

# 작은 그림을 전부 해싱해둠
s_hashes = []
for s in spic:
  s_hashes.append(hashing(s, None))

def checkPic(r, c):
  # 두 번째 행부터 작은 그림 영역만큼 같은 문자열인지 조사
  for i in range(1, sh):
    if (hashing(bpic[r+i][c:sw+c], None) == s_hashes[i] and spic[i] == bpic[r+i][c:sw+c]):
      continue
    else:
      return 0
  return 1
      

for r in range(bh-sh):
  for c in range(bw-sw):
    print(bpic[r][c:sw+c])
    if(c==0):
      b_hash = hashing(bpic[r][:sw], None)

    b_hash = (d*(b_hash - hashing(bpic[r][c-1], -1)) + hashing(bpic[r][sw+c-1], sw+c-1)) % q # 검사 문자열에서 빠져나가는 문자(기존 문자열 맨앞)의 해시값을 빼고 검사 문자열에 추가되는 문자(맨뒤)의 해시값을 더함

    # 작은 그림 첫 번째 줄과 해시값을 비교 && 해시값 충돌일 수 있으니 문자열이 정확히 같은지도 확인
    if(s_hashes[0] == b_hash and spic[0] == bpic[r][c:sw+c]):
      cnt += checkPic(r,c)
      

print(cnt)