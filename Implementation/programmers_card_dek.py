def solution(cards1, cards2, goal):
    answer = 'Yes'
    first = 0 # 첫번째 카드뭉치 확인할 위치가 담김
    second = 0 # 두번째 카드 뭉치 확인할 위치가 담김

    for i in range(len(goal)):
        # cards1의 크기가 first보다 크고 cards1에서 확인할 위치가 goal에
        # 오는 값과 같다면 first의 값을 1 더함
        if len(cards1) > first and cards1[first] == goal[i]:
            first += 1
        # cards2의 크기가 second보다 크고 cards2에서 확인할 위치가 goal에 
        # 오는 값과 같다면 second의 값을 1 더함
        elif len(cards2) > second and cards2[second] == goal[i]:
            second += 1
        else:
            answer = 'No' # card1과 card2에서 goal에 와야하는 단어가 올 수 없다면 answer = 'No'
            break
        
    return answer


