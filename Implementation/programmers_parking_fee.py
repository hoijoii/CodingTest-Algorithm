"""
주차 요금 계산
https://school.programmers.co.kr/learn/courses/30/lessons/92341

차량별 주차요금 계산
주차요금배열 fees: 기본시간(분), 기본요금, 단위시간(분), 단위요금
자동차의 입/출차내역 records : 시각, 차량번호, 입/출차
return 차량번호가 작은 자동차부터 청구할 주차요금을 차례로 배열

주차요금 공식: 기본요금+|(누적주차시간(분)-기본시간(분))/단위시간(분)| x 단위요금

1. 누적주차시간 < 기본시간: 기본요금 청구
2. 초과한시간이 단위시간으로 나누어떨어지지 않으면 올림

먼저 토탈 시간부터 계산 -> 토탈 시간으로 주차요금 계산
변수를 줄여서 다시 풀어보기..?
"""
import math

def solution(fees, records):
    answer = []
    parked = {}
    parkingTime = {record.split(' ')[1]: 0 for record in records} #주차시간

    for record in records:
        time, vehicle, inout = record.split(' ')

        if inout == 'IN':
            parked[vehicle] = time
        else:
            income = list(map(int, (parked[vehicle].split(':'))))
            outgo = list(map(int, time.split(':')))

            if outgo[1]>=income[1]:
                parkingTime[vehicle] += (outgo[0]-income[0])*60 + (outgo[1]-income[1])
            else:
                parkingTime[vehicle] += (outgo[0]-income[0]-1)*60 + (outgo[1]+60-income[1])
        
            parked.pop(vehicle, None) # 출차 처리

    # 만약 parked에 차량이 남아있으면 23:59에 출차 처리.
    if parked:
        for vehicle in parked:
            income = list(map(int, (parked[vehicle].split(':'))))
            parkingTime[vehicle] += (23-income[0])*60 + (59-income[1])

    # 주차시간에 따른 주차요금 계산
    for vehicle in parkingTime:
        if parkingTime[vehicle] < fees[0]:
            parked[vehicle] = fees[1]
        else :
            parked[vehicle] = fees[1] + math.ceil((parkingTime[vehicle]-fees[0])/fees[2])*fees[3]

    answer = list(item[1] for item in sorted(parked.items()))
    return answer

solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
#[14600, 34400, 5000]