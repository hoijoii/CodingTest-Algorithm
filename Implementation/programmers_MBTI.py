def solution(survey, choices):
    answer = ''
    num = [0, 3, 2, 1, 0 ,1 ,2, 3] # 1인덱스부터 매우비동의~매우동의

    score = dict() # 키값쌍으로 점수저장
    for x in "RTFCMJAN":
        score[x] = 0

    #설문조사 점수
    for i in range(len(choices)):
        query = survey[i]

        for q in ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]:
            if q == query:
                if choices[i] < 4:
                    score[q[0]] += num[choices[i]]
                else:
                    score[q[1]] += num[choices[i]]

    #유형만들기
    for x in ["RT","CF","JM","AN"]:
        if score[x[0]] < score[x[1]]:
            answer += x[1]
        else:
            answer += x[0]
    return answer


