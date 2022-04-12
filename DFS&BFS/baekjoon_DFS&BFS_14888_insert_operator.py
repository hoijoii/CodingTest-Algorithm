n = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
result = A[0]

# 최소값과 최대값이 항상 10억보다 작거나 같고, 항상 -10억보다 크거나 같다.
minVal = 1000000000
maxVal = -1000000000

# 변수: 더하기, 빼기, 곱하기, 나누기, 몇 번째 숫자인지 알려주는 변수, 계산 결과
def dfs(add, sub, mul, div, x, result):
    global minVal, maxVal
    # 사칙연산 개수를 다 사용했으면 마지막 연산의 결과를 출력
    if x == n-1:
        if result < minVal:
            minVal = result
        if result > maxVal:
            maxVal = result
    # 사칙연산 진행
    if add > 0:
        dfs(add-1, sub, mul, div, x+1, result + A[x+1])
    if sub > 0:
        dfs(add, sub-1, mul, div, x+1, result - A[x+1])
    if mul > 0:
        dfs(add, sub, mul-1, div, x+1, result * A[x+1])
    if div > 0:
        dfs(add, sub, mul, div-1, x+1, int(result / A[x+1]))

dfs(add, sub, mul, div, 0, result)

print(maxVal)
print(minVal)