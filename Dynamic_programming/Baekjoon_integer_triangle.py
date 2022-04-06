n = int(input())
tri = []
d = [[0] * n for _ in range(n)] # DP테이블

for _ in range(n):
    tri.append(list(map(int, input().split())))

d[0][0] = tri[0][0] # 맨 꼭대기 원소를 넣음

for r in range(1, n):
    for c in range(len(tri[r])):
        # 맨 왼쪽 열이면 오른쪽 대각선 위의 원소와 더함
        if c == 0:
            d[r][c] = d[r-1][c] + tri[r][c]
        # 삼각형의 오른쪽 끝 원소면 왼쪽 대각선 위의 원소와 더함
        elif d[r-1][c] == 0:
            d[r][c] = d[r-1][c-1] + tri[r][c]
            break
        # 삼각형의 중간 부분이면 왼쪽, 오른쪽 대각선 위의 원소 중 더 큰 값의 원소와 더함
        else:
            d[r][c] = max(d[r-1][c-1], d[r-1][c]) + tri[r][c]

# 마지막 행의 원소 중 최대값 출력
print(max(d[n-1]))