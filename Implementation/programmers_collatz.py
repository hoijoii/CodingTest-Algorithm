def collatz(num, count):
    if num%2==0:
        num = num/2
    else: 
        num = num*3+1
    print(num)
    if num != 1:
        count += 1
        print(count)
        if count == 500:
            return -1
        collatz(num, count)

    return count

def solution(num):
    answer = 0
    count = 0

    if num == 1: answer=0
    else: answer=collatz(num, count)

    print(answer)

solution(6)