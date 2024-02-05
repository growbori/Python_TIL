'''
5 x 5 2차 배열에 25의 숫자를 저장하고,

대각선 원소의 합을 구하시오. 대각선 원소는 다음과 같은 위치의 원소를 나타낸다.
'''

N= int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    total += arr[i][i]
    total += arr[i][N-1-i]
if N%2 : # 크기가 홀수인 경우
    total -= arr[N//2][N//2]
print(total)