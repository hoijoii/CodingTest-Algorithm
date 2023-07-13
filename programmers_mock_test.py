"""
1: 1~5순서대로
2: 2,1,2,3,2,4,2,5,2,1,2,3,... 꼭 2를 찍고 다른 숫자를 찍음.
3: 3,3,1,1,2,2,4,4,5,5,... 31245를 각 숫자마다 두번씩 찍음.
완전탐색으로 풀기 ..
"""

def solution(answers):
    answer = []

    pattern = {1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    supoja = {1: 0, 2: 0, 3: 0}
    
    for i in range(len(answers)):
        if answers[i] == pattern[1][i%len(pattern[1])]:
            supoja[1] += 1
        if answers[i] == pattern[2][i%len(pattern[2])]:
            supoja[2] += 1
        if answers[i] == pattern[3][i%len(pattern[3])]:
            supoja[3] += 1

    answer = [k for k, v in supoja.items() if max(supoja.values()) == v]

    return answer

#solution([1, 2, 3, 4 ,5])