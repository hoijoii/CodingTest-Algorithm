"""
가장 큰 수
https://school.programmers.co.kr/learn/courses/30/lessons/42746

cmp_to_key
https://speedy-hand.tistory.com/26
"""
from functools import cmp_to_key

def comparator(a, b):
    return (int(a+b)>int(b+a)) - (int(a+b)<int(b+a)) # a+b가 크면 1, b+a가 크면 -1, 같으면 0

def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(key=cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(numbers)))
    return answer
