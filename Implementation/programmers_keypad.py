"""
123
456
789
*0#

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

def findNumber(num, keypad):
    for i, row in enumerate(keypad):
        if num in row:
            return (i, row.index(num))
        
def dfs(rhand, lhand, keypad) :
    
            
def solution(numbers, hand):
    
    result = ""
    
    keypad = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9],
        ['*', 0, '#']
        ]
    
    rhand = keypad[3][2]
    lhand = keypad[3][0]

    r_len = 0
    l_len = 0

    for num in numbers:
        row, col = findNumber(num, keypad)
        if num == 1 or num == 4 or num == 7: 
           result+='L'
           lhand = keypad[row][col]
           
        elif num == 3 or num == 6 or num == 9: 
           result+='R'
           rhand = keypad[row][col]
        #2, 5, 8, 0일 때 ..
        else:
            
            
            

    print()



    

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")