"""
할인행사
https://school.programmers.co.kr/learn/courses/30/lessons/131127

원하는 제품 나열: want
원하는 제품 수량: number
할인하는 제품: discount

딕셔너리에 want, number를 정리
회원등록날짜를 day로 해서 discount의 길이까지 반복
회원된 날부터 10일 뒤까지 물건을 전부 구할 때까지 반복
만약 세일품목이 쇼핑리스트 중에 있으면 해당 물품 number 하나 감소
number가 0이면 딕셔너리에서 삭제 -> 딕셔너리가 비면 원하는 거 다 얻었다는 것 -> answer+=1
"""
import copy

def solution(want, number, discount):
    answer = 0

    #쇼핑리스트. want, number를 딕셔너리로 정리
    shopping = { want[i] : number[i] for i in range(len(want)) }

    for day in range(len(discount)):
        copied = copy.deepcopy(shopping)
        for d in range(day, day+10 if len(discount)>=day+10 else len(discount)):
            sale = discount[d] # 세일 품목
            if sale in copied:
                copied[sale] -= 1 # 원하는 물품을 할인받으면 개수 하나 줄임
                if copied[sale] == 0 : copied.pop(sale, None) # 물품 수가 0이 되면 쇼핑리스트에서 지움
            # 원하는 물품을 10일 안에 다 얻으면
            if len(copied) == 0:
                answer+=1
                break

    return answer