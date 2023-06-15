def collatz(n, cnt):
  if n > 1: 
     if n%2 == 0 : n=n/2
     else: n=n*3+1
  return n

def solution(num):
    answer = 0
    if num == 1: 
      answer = 0
    elif num != 1: 
      count = 0
      answer = collatz(num, count)

    print(collatz(num, count))

solution(7)