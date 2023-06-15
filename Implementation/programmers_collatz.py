def collatz(n, cnt):
  if n > 1: 
    if n%2 == 0 : n=n/2
    else: n=n*3+1
    cnt+=1
    return collatz(n, cnt)

  elif n==1:
    return cnt

def solution(num):
    answer = 0
    answer = collatz(num, answer)
    if answer > 500:
       answer = -1

    return answer


"""
재귀 안 쓰고 풀기
 
def solution(num):
  answer=0 #count

  while num != 1:
    if num%2==0: 
      num=num/2
    else: 
      num=num*3+1
    
    answer+=1
    if answer > 500: return -1

  return answer

print(solution(6)) """