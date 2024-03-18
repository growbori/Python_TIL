a, b = int(input())

result = 0

for i in range(a):
    arr = list(map(int, input().split()))

    min_value = min(arr)

    result = max(min_value)

print(result)
