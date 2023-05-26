def solution(park, routes):
    answer = []
    
    directions = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

    # S찾기
    for r in range(len(park)):
      for c in range(len(park[r])):
          if park[r][c] == 'S':
            answer=[r, c]
            break

    for route in routes:
      compass, distance = route[0], int(route[2])

      for _ in range(distance) :
        expect = [answer[0]+directions[compass][0], answer[1]+directions[compass][1]]

        if park[expect[0]][expect[1]] == 'X' or (expect[0]>=len(park[0]) or expect[0]<0) or (expect[1]>=len(park) or expect[1]<0):
          break;
        
        else:
          answer = expect

    return answer

print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))