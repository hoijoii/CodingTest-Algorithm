"""
카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842

테스트케이스 규칙: brown+yellow = answer[0]*answer[1]
=> brown+yellow의 약수 = brown의 가능한 가로세로 길이
brown=24, yellow=24일 때 예시

00000000
01111110
01111110
01111110
01111110
00000000

brown가로-2 == yellow가로 and brown세로-2 == yellow세로
인 값을 찾으면 됨.
"""
# 약수 구하는 함수
def divisor(num): 
    divisors = []

    for i in range(1, int(num**(1/2))+1):
        if num%i == 0:
            divisors.append([int(num/i), i]) #가로가 세로와 같거나 더 김
    
    return divisors

def solution(brown, yellow):
    answer = []

    brownGaroSero = divisor(brown+yellow)
    yellowGaroSero = divisor(yellow)

    for ga, se in brownGaroSero:
        for g, s in yellowGaroSero:
            if ga-2 == g and se-2 == s:
                answer.append(ga)
                answer.append(se)
    
    return answer


"""
다른 방안:
방정식 세워서 근의 공식으로 brown의 값을 구할 수 있다.

x = (brown-4)/4 + math.sqrt(brown*brown - 8*brown + 16 - 16*yellow)/4
y = (brown-4)/4 - math.sqrt(brown*brown - 8*brown + 16 - 16*yellow)/4
answer = [x+2, y+2]

"""