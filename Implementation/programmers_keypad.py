"""

초기값 - 왼손엄지: * , 오른엄지: #
hand = 왼손잡이/오른손잡이 -> left 혹은 right
규칙 
- 엄지는 상하좌우 한 칸씩 이동 가능
- 왼손만 이용: 1, 4, 7
- 오른손만 이용: 3, 6, 9
- 가운데 2, 5, 8, 0은 현재 키패드에서 가까운 엄지손가락 사용.
  - 만약 두 엄지의 거리가 같으면 오른손잡이는 오른손 왼손잡이는 왼손 사용

- 왼손 사용한경오 L, 오른손사용한경우 R

testcase : [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand: "right"
result: "LRLLLRLLRRL"
"""

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
  cost = abs(location-num)%3
  print(cost)

  return cost

  """ if sub==1 or sub==3: return 1
  elif sub==2 or sub==4 or sub==6: return 2
  elif sub==5 or sub==7 or sub==9: return 3
  elif sub==8 or sub==10: return 4 """

def solution(numbers, hand):
    
    result = ""
    rhand = 10 # #에서 시작
    lhand = 12 # *에서 시작

    for i in range(len(numbers)):
       if numbers[i] == 0 : numbers[i] == 11

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
          """
          elif getLength(rhand, n) == getLength(lhand, n):
              if hand=='right': 
                 result += 'R'
                 rhand = n
              else:
                 result += 'L'
                 lhand = n
          else:
              result += 'R'
              rhand = n
            """
    print(result)

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
