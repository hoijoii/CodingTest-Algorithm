def solution(s):
    N = len(s)

    answer = N

    for x in range(1, N//2 + 1):
        res = ""
        cur = s[:x]
        cnt = 1
        
        for y in range(x, N, x):
            com = s[y: x+y]
            if cur == com: # 반복 되었을 경우
                cnt += 1
            else:
                if cnt == 1: # 압축이 안 됐을 경우
                    res += cur
                else:
                    res += (cur + f'{cnt}')
                    cnt = 1
                cur = com
                
        if cnt == 1:
            res += cur
        else:
            res += (cur + f'{cnt}')

        answer = min(answer, len(res))

    return answer