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
queue에 넣는데 시간 또 걸리잖어~

1. progress를 queue로 사용
2. queue deepcopy한 리스트를 따로 만들기
3. queue를 for문에 넣으면 queue 변형 불가니까 deepcopy한 거 검사하면서 queue를 변형시킴
4. 가장 상위 반복문은 while(queue). queue가 빌 때까지 반복함. 매 반복마다 queue를 deepcopy하기

"""
import copy

def solution(progresses, speeds):
    answer = []

    list = copy.deepcopy(progresses)

    while(progresses):
        cnt = 0
        for i in range(len(list)):
            if(list[i] == -1):
                continue

            list[i] += speeds[i];
            # 값이 100이 넘어도 첫번째 원소거나, 첫번째 원소 뒤따라 있을 때에만 pop 가능
            if(list[i] >= 100 and (i==0 or list[i-1]==-1)):
                progresses.pop(0)
                list[i] = -1
                cnt += 1
        
        if(cnt): 
            answer.append(cnt)
        
    return answer

    