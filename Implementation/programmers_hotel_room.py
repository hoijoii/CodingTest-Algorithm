"""
https://school.programmers.co.kr/learn/courses/30/lessons/64063

"""
import sys
sys.setrecursionlimit(10 ** 6)

def assign(k, r, answer):
    """ if r+1<k and r+1 not in answer:
        answer.append(r+1)
    else:
        assign(k, r+1, answer) """

def solution(k, room_number):
    answer = []

    for r in room_number:
        if r not in answer:
            answer.append(r)
        else:
            assign(k, r, answer)

    return answer