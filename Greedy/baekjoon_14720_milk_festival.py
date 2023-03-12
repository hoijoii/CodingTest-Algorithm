N = int(input())
stores = list(map(int, input().split()))

milk = [0, 1, 2] # 딸기(0) -> 초코(1) -> 바나나(2)

current = 0 # 딸기우유
count = 0 # 마실 수 있는 개수

# current는 0, 1, 2 반복하며 stores 숫자와 비교
for store in stores:
    if store == current:
        count += 1
        current = milk[(current + 1) % 3] # 0, 1, 2 반복

print(count)