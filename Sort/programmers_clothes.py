"""
의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578

result=(headgear수+1)*(eyewear수+1)-1
headgear 2가지 중 1개를 고를 수도 있고 하나도 안 고를 수 있음: 2+1
eyewear 1가지 중 1개 고를 수도, 안 고를 수도: 1+1

"""


def solution(clothes):
    answer = 1

    closet = { part: 0 for name, part in clothes }

    for name, part in clothes:
        closet[part] += 1
    for n in closet.values():
        answer *= (n+1) # (n개 중 한 개를 고르는 경우 + 하나도 안 고르는 경우)

    return answer-1 # 전부 다 안 골랐을 경우 제외
