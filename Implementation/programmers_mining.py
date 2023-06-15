"""
그리디!!
picks: [dia, iron, stone]
광물은 주어진 순서대로만 깨기
한 곡괭이를 써서 피로도 다 쓸 때까지 광물 캠
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

    for (idx, mineral) in enumerate(minerals):
        if totalPicks == 0: break;
        
    #return answer


solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])