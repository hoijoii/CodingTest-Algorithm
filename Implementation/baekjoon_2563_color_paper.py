
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
for i in range(len(lo)) :

    garo = 0
    sero = 0
    
    if i == 0 : black.append(lo[0])

    elif i > 0 :

        for paper in black :
            
            garo = 10 - abs(paper[0] - lo[i][0])
            sero = 10 - abs(paper[1] - lo[i][1])

            if 0 < garo < 10 and 0 <sero < 10 :
                area -= garo*sero
            #print(garo, sero, area)
        
        black.append(lo[i])
        
print(area)