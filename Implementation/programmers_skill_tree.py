"""
스킬트리
https://school.programmers.co.kr/learn/courses/30/lessons/49993

CBD 순서대로 string(예: BACDE)을 검사
C, B, D가 string의 어디에 있는지 찾고 어디 위치에 있는지 idx를 비교해보면 됨.
C의 인덱스보다 B의 인덱스가 더 작으면 C보다 B가 먼저 나왔단 얘기임.

skill: CBD, string: CD
=> B가 없으므로 string.find()의 결과는 -1이고 그 뒤로는 망한 문자열이라 idx를 무한대로 놓음.
=> 나중에는 27이 bf_idx가 되므로 무조건 false됨.
"""

def isValid(skill, string):
    bf_idx = 0 #이전 인덱스
    for i in range(len(skill)):
        idx = string.find(skill[i]) #스킬트리에서 스킬 못 찾으면 -1반환
        if idx == -1 : idx = 27 #무한대
        if idx < bf_idx : return #스킬순서 어긋남
        bf_idx = idx
    return True

def solution(skill, skill_trees):
    answer = 0
    
    for string in skill_trees:
        if isValid(skill, string) : 
            answer+=1

    return answer