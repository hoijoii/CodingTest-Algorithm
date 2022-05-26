import sys
data = list(sys.stdin.readline().rstrip())
intdata = list(map(int, data)) # 문자열의 str 요소들을 int 자료형으로 바꿈.
l = len(data)

left = intdata[0:l//2]
right = intdata[l//2:]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")