'''

부분집합 합 문제 구현하기

10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 계산해보자

10
-7 -5 2 3 8 -2 4 6 9

'''

def f(arr, N):
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
            #     print(arr[j], end = ' ')
            # print(s)
        if s == 0:
            return True
    return False


N = int(input())
arr = list(map(int, input().split()))
print(f(arr, N))






