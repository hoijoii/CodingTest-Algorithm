""" 
흰색 도화지 위에 검은 색종이 100개 이하의 수 n개 붙이기
흰색 도화지: 가로 세로 크기가 100 
검은 색종이: 가로 세로 크기가 10

=> 검은 색종이가 붙을 수 있는 좌표는 90, 90이 최대

색종이가 도화지 밖으로 나가면 안 됨
n이 2 이상일 때는.. ? 좌표들을 생각하면서 풀어나가기 . .
먼저 입력된 숫자들 기준으로 겹쳤는지 아닌지 판단.(변수필요) 만약에 겹치지 않았으면 n * 100 하면 된다.

먼저 입력된 숫자로부터 가로 세로 10을 더한 값보다 작은 죄표값이 들어오면 겹친 것으로 판단

두 넓이를 더한 것에서 겹친 부분을 빼야 함.

- input
첫째줄: 색종이 수 n
둘째 줄: 한 줄에 하나씩 색종이 붙인 위치 (왼쪽으로부터 몇, 아래로부터 몇)

- output
첫째줄에 색종이가 붙은 검은 영역의 넓이 구하기
"""

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





#겹치는 영역 계산
""" for i in range(n):
    garo=0
    sero=0

    if i == 0 : black.append(locations[i]) # 최초의 색종이

    elif i > 0 : 
        for paper in black :
            # garo, sero 둘 중 하나가 기존 영역과 완전 같거나 하나만 같을 때
            if locations[i][0] == paper[0] :
                garo = 10
                if locations[i][1] == paper[1] :
                    sero = 10
                elif paper[1] < locations[i][1] < paper[1]+10 :
                    sero = paper[1] + 10 - locations[i][1]
                elif paper[1] < locations[i][1]+10 < paper[1]+10 :
                    sero = locations[i][1] + 10 - paper[1]

            elif locations[i][1] == paper[1] :
                sero = 10
                #if locations[i][0] == paper[0] : 
                if paper[0] < locations[i][0] < paper[0]+10:
                    garo = paper[0] + 10 - locations[i][1]
                elif paper[0] < locations[i][0]+10 < paper[0]+10:
                    garo = locations[i][0]+10 - paper[0]


            # 가로 겹치는 영역 찾기
            # 안 겹치는 경우
            if locations[i][0]+10 < paper[0] or locations[i][0] > paper[0]+10 :
                garo = 0 
            # 일부 겹치는 경우
            elif paper[0] < locations[i][0]+10 < paper[0]+10 :
                garo = locations[i][0]+10-paper[0]
            # 일부 겹치는 경우
            elif paper[0] < locations[i][0] < paper[0]+10 :
                garo = paper[0]+10-locations[i][0]


            # 세로 겹치는 영역 찾기
            # (안 겹치는 경우)기존 영역보다 아예 아래 or 기존 영역보다 아예 위
            if locations[i][1]+10 < paper[1] or locations[i][1] > paper[1]+10 :
                sero = 0
            elif paper[1]<locations[i][1]+10<paper[1]+10:
                sero = locations[i][1]+10 - paper[1]
            elif paper[1] < locations[i][1] < paper[1]+10 :
                sero = paper[1]+10 - locations[i][1]

            # 겹치는 면적 더하기
            over_area += garo * sero
            
# 전체 면적에서 겹치는 면적을 뺌
area -= over_area

print(area) """
    
#print(locations)
