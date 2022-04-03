# 다른 학생에게 옷을 빌려주기 전 lost와 reverse의 중복 요소를 제거하는 것이 관건인 문제

def solution(n, lost, reverse):

    lost.sort()
    reverse.sort()

    new_reverse = [i for i in reverse if i not in lost]
    new_lost = [i for i in lost if i not in reverse]

    for i in new_reverse:
        if i - 1 in new_lost:
            new_lost.remove(i - 1)

        elif i + 1 in new_lost:
            new_lost.remove(i + 1)

    answer = n-len(new_lost)

    return answer
