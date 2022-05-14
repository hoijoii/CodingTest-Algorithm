t = int(input())  # 테스트 케이스 T
gold = []
mine = []

for _ in range(t):
    n, m = map(int, input().split())  # m:열, n:행
    gold = list(map(int, input().split()))  # 금광 일렬로 입력받음

    mine = [gold[i * m:(i + 1) * m] for i in range((len(gold) + m - 1) // m)]  # 일렬로 입력받은 금광을 2차원 리스트로 나타냄
    d = [[0] * m for _ in range(n)]  # 최댓값들을 저장할 2차원 리스트

    for i in range(n):
        d[i][0] = mine[i][0]  # 첫 번째 열의 원소들은 그냥 넣음

    # 문제에서 오른쪽 위, 오른쪽, 오른쪽 아래로 이동한다고 설명하였는데,
    # 이동한 다음 원소 기준으로 보면 왼쪽 위, 왼쪽, 왼쪽 아래에서 이동해왔다고 볼 수 있다.
    for c in range(1, m):
        for r in range(n):
            if r == 0:
                # 맨 위 행일 경우 왼쪽 위가 없음. 왼쪽, 왼쪽 아래 중 큰 값을 더함.
                d[r][c] = max(d[r][c - 1], d[r + 1][c - 1]) + mine[r][c]
            elif r == n - 1:
                # 맨 아래 행일 경우 왼쪽 아래가 없음. 왼쪽, 왼쪽 위 중 큰 값을 더함.
                d[r][c] = max(d[r][c - 1], d[r - 1][c - 1]) + mine[r][c]
            else:
                # 맨 위, 맨 아래 행이 아닐 경우. 왼쪽, 왼쪽 위, 왼쪽 아래 중 가장 큰 값을 더함.
                d[r][c] = max(d[r][c - 1], d[r + 1][c - 1], d[r - 1][c - 1]) + mine[r][c]

    answer = []
    for j in range(n):
        answer.append(d[j][m - 1])
    # 마지막 열의 숫자들 중 최대값을 구함
    print(max(answer))
