"""
타겟넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165

정수를 순서 안 바꾸고 더하거나 빼서 타겟 넘버 만들기
방법의 수를 리턴하면 됨.
"""

def solution(numbers, target):
    answer = 0
    def dfs(depth, totalSum):
        nonlocal answer
        if depth == len(numbers):
            if totalSum == target: answer += 1
            return 
    
        dfs(depth+1, totalSum+numbers[depth])
        dfs(depth+1, totalSum-numbers[depth])
    
    dfs(0, 0)

    return answer
