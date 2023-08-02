"""
callings에서 가져온 플레이어를 찾을 때 players 전체 검색 안하도록
딕셔너리에서 바로 찾아옴
"""

def solution(players, callings):
    # 플레이어 등수 기록
    rank = { player : idx for idx, player in enumerate(players) }

    for c in callings:
        ahead = rank[c]-1 
        behind = rank[c] 
        # 기록된 등수 변경
        rank[players[ahead]], rank[players[behind]] = behind, ahead
        # 실제 순서 변경
        players[ahead], players[behind] = players[behind], players[ahead]

    return players

