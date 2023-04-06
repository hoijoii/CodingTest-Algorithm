"""
input: new_id

문자열 변환 조건
1. 모든 대문자 -> 소문자
2. 소문자, 숫자, -, _, . 제외 모든 문자 제거
3. 마침표(.)가 2번 이상 연속되면 하나의 .로 치환
4. .가 처음이나 끝에 위치하면 제거
5. new_id가 빈 문자열이면 new_id에 a 대입
6. new_id 길이가 16자 이상이면 new_id의 첫 15개 문자 제외한 나머지 문자들을 제거, 제거 후 .가 마지막에 위치하면 . 제거
7. new_id 길이가 2자 이하면 new_id 마지막 문자를 new_id 길이가 3이 될 때까지 반복해 끝에 붙임
"""
def stEdPeriod(alter):
    if alter[0] == '.' : alter = '' + alter[1:]
    if len(alter):
      if alter[-1] == '.' : alter = alter[:len(alter)-1] + ''
    
    return alter

def solution(new_id):
    alter = []

    # 1. 대문자 -> 소문자
    new_id = new_id.lower()

    # 2. 소문자, 숫자, -, _, . 제외 모든 문자 제거
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i =='_' or i == '.':
            alter.append(i)

    # 3. 마침표가 2번 이상 연속되면 하나의 마침표로 치환
    pre_letter = ''
    for i in range(1, len(alter)):
        pre_letter = alter[i-1]
        if alter[i] == '.' and alter[i] == pre_letter:
            alter[i-1] = ''

    # 4. .가 처음이나 끝에 위치하면 제거
    alter = "".join(alter)
    alter = stEdPeriod(alter)

    # 5. new_id가 빈 문자열이면 new_id에 a 대입
    if not alter: alter = 'a'

    # 6. new_id 길이가 16자 이상이면 new_id의 첫 15개 문자 제외한 나머지 문자들을 제거, 제거 후 .가 마지막에 위치하면 . 제거
    if len(alter) >= 16: 
       alter = alter[:15]
       alter = stEdPeriod(alter)

    # 7. new_id 길이가 2자 이하면 new_id 마지막 문자를 new_id 길이가 3이 될 때까지 반복
    if len(alter) <= 2:
      while(len(alter)<3):
          alter += alter[-1]
            
    return alter
