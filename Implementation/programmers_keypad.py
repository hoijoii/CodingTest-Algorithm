"""
1 2 3
4 5 6
7 8 9
* 0 #

*:10, 0:11, #:12

가장 큰 이동 cost 4

이동 cost 1일 때 숫자 차이 = 1 or 3
이동 cost 2일 때 숫자 차이 = 2 or 4 or 6 
이동 cost 3일 때 숫자 차이 = 5 or 7 or 9
이동 cost 4일 때 숫자 차이 = 8 or 10

=> (location-num)%3 = cost

"""

def getLength(location, num):
  sub = abs(location-num)

  if sub==1 or sub==3: return 1
  elif sub==2 or sub==4 or sub==6: return 2
  elif sub==5 or sub==7 or sub==9: return 3
  elif sub==8 or sub==10: return 4
  elif sub==0 : return 0 # 같은 번호를 두 번 누르는 경우

def solution(numbers, hand):
    
    result = ""
    rhand = 12 # #에서 시작
    lhand = 10 # *에서 시작

    while(0 in numbers) :
        numbers[numbers.index(0)] = 11

    for n in numbers:
        if n==1 or n==4 or n==7:
          result+='L'
          lhand = n    
        elif n==3 or n==6 or n==9:
          result+='R'
          rhand = n
        else:
          if getLength(lhand, n) < getLength(rhand, n) :
             result+='L'
             lhand=n
          elif getLength(rhand, n) == getLength(lhand, n):
              if hand == "right":
                result+='R'
                rhand = n
              else:
                  result += 'L'
                  lhand = n
          else:
              result += 'R'
              rhand = n

    return result