N, M, K = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse= True)

first = arr[0]
second = arr[1]

result = 0

while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M == 0: # M이 0이라면 반복문 탈출
            break
        result += first
        M -=1 # 더할 때 마다 1씩 빼기
    if M == 0: #M이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    M-=1 # 더할 때 마다 1씩 빼기

print(result)

'''
5 8 3
2 4 5 4 6


'''