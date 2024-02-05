N, M, K = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse= True)

first = arr[0]
second = arr[1]

count = int(M/(K+1)) * K
count += M % (K+1) # M이 (K+1)로 나누어 떨어지지 않는 경우 나머지

result = 0
result += (count) * first
result += (M-count) * second

print(result)

'''
5 8 3
2 4 5 4 6

'''