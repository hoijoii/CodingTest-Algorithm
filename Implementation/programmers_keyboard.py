def solution(keymap, targets):

    answer = []
    keyCount = dict() # 각 문자를 최소한으로 눌러 얻을 수 있는 수를 저장 => 문자별로 숫자 정리

    for key in keymap:
        for idx, v in enumerate(key):
            # 현재 인덱스 vs 기존 인덱스 더 작은 걸 저장
            keyCount[v] = min(idx+1, keyCount[v] if v in keyCount else 100)
    
    for string in targets:
        cnt = 0
        for s in string:
            if s in keyCount:
                cnt += keyCount[s]
            else:
                cnt = -1
                break
        
        answer.append(cnt)

    return answer