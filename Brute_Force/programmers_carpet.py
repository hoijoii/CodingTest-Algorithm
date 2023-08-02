"""
카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842

brown: 갈색 격자의 수
yellow: 노란색 격자의 수
카펫의 가로, 세로크기를 배열에 담아 return

카펫의 가로길이는 세로길이와 같거나 길다

직사각형을 어떻게 만드느냐 ?
return 값인 배열의 두 값을 곱했을 때 brown+yellow값이 나옴 왜냐면 넓이공식이니까
brown+yellow 값의 약수를 다 구해서..?

"""

def divisor(num): 
    data = set()

    for i in range(1, int(num**(1/2))+1):
        if num%i == 0:
            data.add(i)
            data.add(num//i)
        return sorted(data)

def solution(brown, yellow):
    answer = []

    print(divisor(24))
    
    return answer

solution(24, 24)