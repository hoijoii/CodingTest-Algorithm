def solution(lottos, win_nums):
    # 순위를 return하는 함수
    def rank(count) :
        if count == 6 :
            return 1
        elif count == 5 :
            return 2
        elif count == 4 :
            return 3
        elif count == 3 :
            return 4
        elif count == 2 :
            return 5
        else :
            return 6
        
    count = 0
    for i in lottos :
        if i in win_nums :
            count += 1
    zero = lottos.count(0)
    answer = [rank(count+zero), rank(count)]
    return answer



