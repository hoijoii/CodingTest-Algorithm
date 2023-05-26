def move(answer, blockCnt, st, ed):
    temp = 2 # temp는 st에서 ed로 가기 위한 중간과정 기둥
    # 중간과정 기둥을 결정
    # range(1, 4): 1, 2, 3
    for i in range(1, 4):
        if i != st and i != ed:
            temp = i

    if blockCnt==1:
        answer.append([st, ed])
    else:
        move(answer, blockCnt-1, st, temp) 
        answer.append([st, ed]) # 맨 밑 블록을 3번기둥에 옮김
        move(answer, blockCnt-1, temp, ed) # 나머지 블럭에 있던 걸 3번기둥에 옮기면 됨

def solution(n):
    answer = []
    move(answer, n, 1, 3)
    return answer