"""
1~10001을 리스트에 저장, 생성자면 리스트에서 삭제
"""

# 생성자인지 확인하고 삭제하는 함수
def check(num, arr):
    # num을 문자열로 바꾸고 -> 다시 정수로 바꿈 한 자리씩 더함
    for n in str(num):
        num += int(n)
    # num이 arr에 있으면 arr에서 num을 지움
    if arr.count(num) > 0:
        arr.remove(num)

if __name__ == '__main__':
    # 1~10001 담긴 리스트
    selfNumber = list(range(1,10001))
    
    for i in range(1, 10000):
        check(i, selfNumber)

    for i in selfNumber: 
        print(i)