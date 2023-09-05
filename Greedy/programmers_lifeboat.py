"""
구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""

def solution(people, limit):
    answer = 0
    light_idx=len(people)-1

    people.sort(reverse=True)

    for i in range(len(people)):
        if i < light_idx:
            if people[i] + people[light_idx] <= limit:
                light_idx -= 1
            answer+=1
        elif i == light_idx: answer+=1 # people 홀수인 경우

    return answer
