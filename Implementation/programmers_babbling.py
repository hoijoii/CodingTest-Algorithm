import re
def solution(babbling):
    answer = 0
    word = ['aya','ye','woo','ma'] # 발음할 수 있는 단어
    
    for b in babbling:
        for text in word:
            if text * 2 not in b:
                b = b.replace(text, ' ')
        if b.strip() == '':
            count += 1

    return answer




