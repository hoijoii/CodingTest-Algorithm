"""
42586 - 기능개발

progresses: 먼저 배포되어야 하는 순서(퍼센트)
speeds: 각 작업의 개발 속도(하루마다 몇 퍼센트씩 완료되는지)
return값: 각 배포마다 몇 개의 기능이 배포되는가

progresses: [93, 30, 55]
speeds: [1, 30, 5]
return: [2, 1] // 7일 째에 2개, 9일째에 1개 배포
앞 작업이 완료 되어야 뒷 작업도 배포할 수 있음. (뒷 작업이 완료되어도 앞 작업이 완료 안 되었으면 배포 X)

일단 queue에 progresses를 다 넣기
조건에 따라 queue에서 제거하는데..
어차피 앞에 거 완료 못하면 뒤에 거 못 빼니까 queue 의미가 있나?
"""
""" def checkFinish(list):
    for i in range(len(list)):
        if(list[i] == 100):
            return True """

def solution(progresses, speeds):
    answer = []

    for i in range(len(progresses)):
        if(progresses[i] == 100):


        progresses[i] += speeds[i]

    return answer