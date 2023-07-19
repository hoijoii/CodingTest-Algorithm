"""
타겟넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165

정수를 순서 안 바꾸고 더하거나 빼서 타겟 넘버 만들기
방법의 수를 리턴하면 됨.
dfs.. 모든 숫자를 거쳐야하고 모든 방법을 알아야 하니까

맨처음은 전부 플러스.
하나씩 -로..?
-의 수와 위치
몇 개씩 묶으면서 연산?
"""

def dfs(numbers, target, cnt):
    #검사&연산
    #group = 0
    lo = 0
    sum_val = 0
    for g in range(1, len(numbers)):
        #group += 1
        for i in range(len(numbers)):
            #negative = -numbers[lo]
            if lo == i:
                sum_val += -numbers[i]
            sum_val += numbers[i]
            lo += 1       

def solution(numbers, target):
    answer = 0

    dfs(numbers, target, answer)
    

    return answer