"""
추월했을 때 이름이 불림.
players: 1등부터 순서대로 담긴 배열

.index()는 O(N)임 .. 쓰지말기

answer에 이름을 집어넣는데
만약 그 이름이 callings 안에 없으면 그대로 append,
이름이 있으면 몇 개인지 세고 인덱스 그만큼 앞에서 append ?


def solution(players, callings):
    answer = []
    rank = { player : idx for idx, player in enumerate(players) }

    def getKey(val):
        for key, value in rank.items():
            if val == value:
                return key

    for c in callings:
        rank[getKey(rank[c]-1)] += 1
        rank[c] -= 1

    answer = sorted(rank, key = lambda x : rank[x])

    return answer
"""

def solution(players, callings):
    answer = ['' for _ in range(len(players))]
    rank = { player : idx for idx, player in enumerate(players) }

    for c in callings:
        rank[c] -= 1
        

    for key, value in rank.items():
        answer[value] = key

    print(answer)

    return answer

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])