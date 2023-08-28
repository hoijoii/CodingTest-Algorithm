"""
의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578

["의상", "신체부위"]
가능한 조합 개수 return
"""

def combination(closet, n):
    for cloth in closet:
        

def solution(clothes):
    answer = 0

    closet = { part: 0 for cloth, part in clothes }

    for cloth in clothes:
        closet[cloth[1]] += 1

    for i in range(1, len(closet.items())+1):
        combination(closet, i)

    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])