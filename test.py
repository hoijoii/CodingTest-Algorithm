def solution(triangle):
    answer = 0

    dp = [[0]*len(triangle) for _ in range(len(triangle))]

    dp[0][0] = triangle[0][0] # 맨 꼭대기 원소를 넣음

    for r in range(1, len(triangle)):
        for c in range(len(triangle[r])):
            # 맨 왼쪽 열이면 오른쪽 대각선 위의 원소와 더함
            if c==0:
                dp[r][c] = dp[r-1][c] + triangle[r][c]
            # 삼각형의 오른쪽 끝 원소면 왼쪽 대각선 위의 원소와 더함
            elif dp[r-1][c] == 0:
                dp[r][c] = dp[r-1][c-1] + triangle[r][c]
                break
            # 삼각형의 중간 부분이면 왼쪽, 오른쪽 대각선 위의 원소 중 더 큰 값의 원소와 더함
            else:
                dp[r][c] = max(dp[r-1][c-1], dp[r-1][c]) + triangle[r][c]

    answer = max(dp[len(triangle)-1]) # 마지막 행의 원소 중 최대값
    return answer