def move(answer, blockCnt, st, ed):
    temp = 2 # temp: 중간과정
    # range(1, 4): 1, 2, 3
    for i in range(1, 4):
        if i != st and i != ed:
            temp = i

    if blockCnt==1:
        answer.append([st, ed])
    else:
        move(answer, blockCnt-1, st, temp) # 일단 나머지 기둥에 옮김
        answer.append([st, ed]) 
        move(answer, blockCnt-1, temp, ed) 

def solution(n):
    answer = []
    move(answer, n, 1, 3)

    return answer

solution(3)


# print('move('+str(answer)+','+str(blockCnt)+','+str(st)+','+ str(ed)+')')
