import sys
data = list(sys.stdin.readline().rstrip()) # 문자열 입력받음

data.sort() # 알파벳과 숫자 오름차순 정렬. 숫자가 먼저 정렬됨.
result = list() # 결과를 저장할 리스트
sum = 0

for i in data:
    if i.isdigit(): # 숫자면 참을 반환하는 함수
        sum += int(i) # 만약 요소가 숫자라면 더함
    else:
        result.append(i) # 숫자가 아니라면 리스트에 추가
result.append(str(sum)) # 더해진 숫자가 int 이므로 str 로 바꿔줌

print(''.join(result)) # 문자열을 ''와 공백 제외하고 붙여서 출력
