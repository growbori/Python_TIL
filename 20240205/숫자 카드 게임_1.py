N, M = map(int, input().split())

result = 0

for i in range(N):
    arr = list(map(int, input().split()))

    min_card = 10001
    for a in arr:
        min_card = min(min_card, a)

    result = max(result, min_card)

print(result)