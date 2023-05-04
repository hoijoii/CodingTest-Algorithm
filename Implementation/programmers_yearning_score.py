def solution(name, yearning, photo):
    answer = []
    score = dict()

    for idx, v in enumerate(name):
        score[v] = yearning[idx]
    
    for p in photo:
        cnt = 0
        for person in p:
            if person in score:
                cnt += score[person]
        
        answer.append(cnt)

    return answer