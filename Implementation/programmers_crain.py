def solution(board, moves): 
    count = 0 # 인형 터지는 횟수
    stack = [] # 바구니

    for m in moves:
        # board가 옆으로 누워있으므로 row
        for row in board:
            # 열에서 인형을 뽑음
            # m은 +1된 인덱스라서 빼줌 
            if row[m-1] != 0:
                stack.append(row[m-1])
                row[m-1] = 0 # 뽑은 인형 자리 0표시
                break

    flag = 0
    while flag == 0:
        if len(stack <= 1):
            break
        for doll_num in range(len(stack)):
            if stack[doll_num] == stack[doll_num+1]:
                stack.pop(doll_num)
                stack.pop(doll_num)
                count+=1
                break
            # out of range 방지
            if doll_num == len(stack)-2:
                flag = 1
                break

    return count * 2
