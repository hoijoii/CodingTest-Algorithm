"""
그리디!!
picks: [dia, iron, stone]
광물은 주어진 순서대로만 깨기
한 곡괭이로 5개 광물 연속으로 캐기

연속된 5개의 광물을 연속으로 캐야 함
-> 연속된 5개를 하나의 그룹으로 생각하기
-> 다이아/철/돌 사용했을 때 피로도를 그룹별로 리스트에 저장
-> 돌곡괭이 사용했을 때의 피로도를 기준으로 내림차순 정렬,(왜냐면 최악의 경우니까)
-> 정렬된 순서대로 현재 갖고 있는 최선의 곡괭이를 사용했을 때 피로도를 정답에 더해주기

"""

def solution(picks, minerals):
    answer = 0
    # 피로도 표. 열: 광물 / 행: 곡괭이
    pirodo = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]

    totalPicks = sum(picks)
    pirodo_list = [] # 5개씩 부술 때 곡괭이마다 드는 피로도 [dia, iron, stone]

    #한 곡괭이로 5개 캐야 하니까 5개 아예 묶음
    for i in range(0, len(minerals), 5):
        if totalPicks == 0: break;
        
        dia, iron, stone = 0, 0, 0
        # 5개 묶음 안에서 하나하나 곡괭이 피로도 더해서 리스트에 넣음
        for j in range(i, i+5):
            if j == len(minerals): break;

            val = 0
            if minerals[j] == "diamond": val=0
            elif minerals[j] == "iron" : val=1
            elif minerals[j] == "stone" : val=2

            dia += pirodo[0][val]
            iron += pirodo[1][val]
            stone += pirodo[2][val]

        pirodo_list.append([dia, iron, stone]) # 5개 묶음을 부술 때 필요한 피로도 리스트에 추가
        totalPicks -= 1

    pirodo_list.sort(reverse=True, key=lambda x:x[2]) # 돌곡괭이 기준 내림차순

    # 피로도가 적게 드는 곡괭이로 많은 광물을 캘수록 좋음. => 내림차순해둔 리스트 돌면서 다이아 곡괭이부터 소진.
    for p in pirodo_list:
        dia = p[0]
        iron = p[1]
        stone = p[2]

        if picks[0] > 0:
            answer+=dia
            picks[0] -= 1
            continue
        if picks[1] > 0:
            answer+=iron
            picks[1] -= 1
            continue
        if picks[2] > 0:
            answer+=stone
            picks[2] -= 1
            continue

    return answer