k = int(input()) # 검은색종이 수
lo = [list(map(int, input().split())) for _ in range(k)]  # 검은색종이 위치 input

dhj = [[0 for _ in range(100)] for _ in range(100)]
result = 0

#좌표에 1 찍기
for l in lo :
    a=99-l[1]
    b=l[0]

    for i in range(a, a-10, -1) :
        for j in range(b, b+10):
            dhj[i][j] = 1


for garo in dhj: 
    for num in garo:
        if num == 1:
            result+=1

print(result)
