def solution(N, stages):
    answer = []
    fail = []
    count = 0
    # 1(스테이지)부터 stages의 원소와 대조
    for i in range(1, N + 1):
        for stage in stages:
            # 스테이지에 도달한 플레이어 수를 셈
            if stage >= i:
                count += 1
        # i 스테이지에 도달한 사람이 없으면 실패율이 0
        if stages.count(i) == 0:
            fail.append([0, i])
        else:
            # 스테이지에 도달했으나 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
            fail.append([stages.count(i) / count, i])
        count = 0
    # 실패율에 따른 내림차순 정렬
    fail.sort(key=lambda x: -x[0])

    for i in range(N):
        answer.append(fail[i][1])

    return answer
