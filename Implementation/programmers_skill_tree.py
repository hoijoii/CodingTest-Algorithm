"""
스킬트리
https://school.programmers.co.kr/learn/courses/30/lessons/49993

모든 문자열 대문자
가능한 스킬트리 개수를 return

index로 비교?만약 C의 인덱스보다 B의 인덱스가 뒤에 있으면 통과
"""

""" def findOrder(skill, skill_trees):
    skillInTree = { s : 0 for s in skill }
    
    for i in skill:
        for string in skill_trees:
            if i in string:
                skillInTree[i] = string.index(i)

    return skillInTree """

"""
skill에 있는 맨앞부터 순서대로 써야함.
skill_trees의 string 인덱스가 높을수록 뒤에 썼다는 의미.

검사할 것
skill의 순서대로 쓰였는지
앞 skill이 안 쓰였는데 뒷 skill이 쓰였는지
 - skill_trees의 index와 비교? 앞에 있는거 차례로 몇개쓰기 ㄱㅊ 뒤에 있는거 차례대로라도 쓰면 안됨
"""

def solution(skill, skill_trees):
    answer = 0
    checked = []
    
    for string in skill_trees:
        for i in skill:
            if i in string:
                checked.append([i, string.index(i)])
        print(checked)
        
        for idx, [skl, tree_idx] in enumerate(checked):
            if skl != skill[idx]: break
            if tree_idx > checked[idx][1]: break
    


        """ if len(checkedIdx) > 1:
            for n in range(len(checkedIdx)-1):
                if checkedIdx[n] < checkedIdx[n+1] and :
                    print('ok')
                    continue
                else: break
                
        else: answer += 1 """

        print('--------------------------')
        checked = []

    print(answer)

    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])