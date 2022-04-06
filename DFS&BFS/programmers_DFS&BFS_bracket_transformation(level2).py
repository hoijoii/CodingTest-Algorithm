def solution(p):
    answer = ''
    u = ''
    v = ''
    c = 0
    # p가 빈 문자열이거나 '올바른 괄호 문자열'이면 그대로 반환
    if good(p) or p == '':
        return p
    # u, v를 나눔
    else:
        k = 0
        l = 0
        for i in p:
            if i == '(':
                k += 1 # '('의 개수를 셈
            else:
                l += 1 # ')'의 개수를 셈
            c += 1
            # u, v 둘 다 '균형잡힌 괄호 문자열'이 되려면 ')'와 '('의 개수가 같아야 함
            if k == l:
                u += p[:c]
                v += p[c:]
                break
        # 만약 u가 '올바른 괄호 문자열'이면 문자열 v에 대해 재귀적으로 수행, 문자열을 이어붙임
        if good(u):
            if v:
                return u + solution(v)
            else:
                return u
        else:
            answer = '(' + solution(v) + ')'
            if u:
                u = u[1:len(u)-1]
                for j in u:
                    if j == '(':
                        answer += ')'
                    else:
                        answer += '('
            return answer

# '올바른 괄호 문자열'
def good(p):
    list = []
    for i in range(len(p)):
        if p[i] == '(':
            list.append(i)
        elif p[i] == ')':
            if list:
                list.pop()
            else:
                return False
    return True

