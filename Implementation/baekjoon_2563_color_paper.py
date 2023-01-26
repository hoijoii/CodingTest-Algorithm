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

n = int(input()) # 검은색종이 수

locations = [] # 검은색종이 위치
black = [] # 검사된 검은색종이 
area = n*100 # 총 넓이
over_area = 0 # 겹친 영역 넓이 계산

for _ in range(n):
    cdnate = list(map(int, input().split()))
    locations.append(cdnate)

#겹치는 영역 계산
for i in range(n):
    garo=0
    sero=0

    if i == 0 : black.append(locations[i]) # 최초의 색종이

    elif i > 0 : 
        print(black.len())
        """ for j in black.len() :
            # 가로가 안 겹치는 경우
            if locations[i][0]+10 < black[j][0] or locations[i][0]>black[j][0]+10 :
                garo = 0 #나중에 세로가 겹치면 garo=10임.
                print(garo) 
             elif black[j][0] < lo """
            

        



#print(locations)
