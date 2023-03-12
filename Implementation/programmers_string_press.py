# 문자열 끊는 단위는 한 번에 한 숫자만 가능
# => 2단위로 끊고 뒤에는 3단위로 끊기 이런거 불가능

# queue? 일단 s를 queue에 다 넣고 하나씩 뺌
# 검사하는 리스트에 queue를 도입하는것도 ? ?

# 방법1: 진짜 문자열을 만듦. aabb => 2a2b로 만든 다음 length 계산
# 방법2: 반복되는 문자열이 있으면 abcabc일 때 반복된 abc를 전체 length에서 빼고 붙는 숫자 길이를 더함

import math

def solution(s):

    unit = 1
    #new_str = '' #새롭게 만들 문자열
    cnt = 0

    if len(s) == 1 :
        return 1

    while(1):
        new_str = ''
        group = ''
        st = 0
        ed = unit

        for _ in range(len(s)//unit):
            group = s[st:ed]
            new_str += group
            st = ed
            ed += unit

        if len

        # unit이 s/2보다 커지면 반복할 수 없음.
        if unit == len(s)//2 :
            break

        unit+=1
        
        
    
    """ unit = 1
    length = len(s)
    start, end = 0

    for i in range(len(s)):
            start = i # 반복 시작 인덱스 """

    """ while(1):
        
        

        if unit == math.floor(len(s)/2) :
            break

        unit+=1 """


    """
        unit_str = ''
        contrast = ''
        for i in range(len(s)):
            for n in range(unit):
                if i+n < len(s):
                    unit_str += s[i+n]
                else: break

            

            
            
            if unit_str == contrast:
                min_length = length - len(unit_str)*repeat + (len(unit_str)+1)
            

            unit_str = ''"""

    """ unit = 1
    length= []

    while(1):
        str = []
        string = ''
        for i in range(len(s)): 
            #s[i]
            for j in range(unit):
                if j < len(s)-i:
                    string += s[i+j] 
            
            str.append(string)
            string = ''
            print(str)

        if unit == math.floor(len(s)/2) :
            break

        unit += 1 """

    """ unit = 1
    length = [] # unit(index)에 해당하는 length 저장

    while(1):
        str = []
        for i in range(s):
            if len(str) == unit :
                str.remove(s[0])
            str.append(s[i])

            
        
        # unit이 s/2 길이만큼 커지면 검사 끝
        if unit == len(s/2) :
            break

        unit+=1 """

    #return max(length)


s = input()

solution(s)