k = int(input()) # 검은색종이 수
lo = [list(map(int, input().split())) for _ in range(k)]  # 검은색종이 위치 input

dhj = [[0 for _ in range(100)] for _ in range(100)] # do hwa ji
result = 0

#좌표에 1 찍기
for l in lo :
    a=99-l[1] #row -> 좌표가 아래서부터 기준이라서 빼줌
    b=l[0] #column

    for i in range(a, a-10, -1) :
        for j in range(b, b+10):
            dhj[i][j] = 1


for garo in dhj: 
    for num in garo:
        if num == 1:
            result+=1

print(result)


"""
<오답노트>

시도한 방법: (검은색 종이들 전체 넓이) - (종이끼리 겹치는 영역 전체 넓이)
but 이중 3중 4중 ... 으로 겹친 영역이 이중 3중 4중 계산돼서 실패

(오답)
k = int(input()) # 검은색종이 수
numbers = [list(map(int, input().split())) for _ in range(k)]  # 검은색종이 위치 input

black = [] # 검사된 색종이

# 중복 제거
lo = []
for n in numbers:
    if n not in lo:
        lo.append(n)

area = len(lo)*100 # 총 넓이

# 겹치는 영역 찾기
# 이중 이상 겹침은 어떻게 해야 ? ?
for i in range(len(lo)) :

    garo = 0
    sero = 0
    
    if i == 0 : black.append(lo[0])

    elif i > 0 :

        for paper in black :
            
            garo = 10 - abs(paper[0] - lo[i][0])
            sero = 10 - abs(paper[1] - lo[i][1])

            if 0 < garo < 10 and 0 < sero < 10 :
                area -= garo*sero

            #print(garo, sero, area)
        
        black.append(lo[i])
        
print(area)


"""