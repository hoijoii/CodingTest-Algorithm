N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

sum = 0

for n in range(N):
    sum += A[n]*B[n]

print(sum)

