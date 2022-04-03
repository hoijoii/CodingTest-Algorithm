
def solution(n, lost, reverse):

    lost.sort()
    reverse.sort()

    attend = [i for i in range(1, n + 1) if i not in lost]

    new_reverse=[]
    new_lost=[]

    for i in reverse:
        if i not in lost:
            new_reverse.append(i)
        else:
            attend.append(i)

    for i in lost:
        if i not in reverse:
            new_lost.append(i)

    for i in new_reverse:
        if i - 1 in new_lost:
            attend.append(i - 1)
            new_lost.remove(i - 1)

        elif i + 1 in new_lost:
            attend.append(i + 1)
            new_lost.remove(i + 1)

    answer = len(attend)

    return answer

print(solution(5, [2, 4], [3, 1]))