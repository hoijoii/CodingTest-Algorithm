"""
그리디!!
picks: [dia, iron, stone]
광물은 주어진 순서대로만 깨기
한 곡괭이로 5개 광물 연속으로 캐기

연속된 5개의 광물을 연속으로 캐야 함
-> 연속된 5개를 하나의 그룹으로 생각하기
-> 다이아/철/돌 사용했을 때 피로도를 그룹별로 리스트에 저장
-> 돌곡괭이 사용했을 때의 피로도를 기준으로 내림차순 정렬,
-> 정렬된 순서대로 현재 갖고 있는 최선의 곡괭이를 사용했을 때 피로도를 정답에 더해주기

https://velog.io/@seowj0710/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level-2-%EA%B4%91%EB%AC%BC-%EC%BA%90%EA%B8%B0-Java
"""

def solution(picks, minerals):
    answer = 0
    # 피로도
    # 열: 광물
    # 행: 곡괭이
    pirodo = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]

    totalPicks = sum(picks)
    pirodo_list = []

    for i in range(0, len(minerals), 5):
        if totalPicks == 0: break;
        
        dia, iron, stone = 0, 0, 0
        for j in range(i, i+5):
            if j == len(minerals): break;

            val = 0
            if minerals[j] == "diamond": val=0
            elif minerals[j] == "iron" : val=1
            else : val=3

            dia += pirodo[0][val]
            iron += pirodo[1][val]
            stone += pirodo[2][val]

        pirodo_list.append([dia, iron, stone])
        totalPicks -= 1

    print(pirodo_list)
    #return answer

solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])

"""

i=0
	j=0
		if 0 == 7 : break x
		val=0
		dia+=1 => dia=1
		iron+=5 => iron=5
		stone+=25 => stone=25
		
	j=1
		if 1 == 7: break; x
		val=0
		dia+=1 => dia=2
		iron+=5 => iron=10
		stone+=25 => stone=50
	j=2
		if 2==7: break; x
		val=0
		dia+=1 => dia=3
		iron+=5 => iron=15
		stone+=25 => stone=75
	j=3
		if 3==7: break; x
		val=1
		dia+=1 => dia=4
		iron+=1 => iron=16
		stone+=5 => stone=80
	j=4
		if 4 ==7: break; x
		val=1
"""