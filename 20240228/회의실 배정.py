'''
10
1 4  1 6  6 10  5 7  3 8  5 9  3 5  8 11  2 13  12 14
'''

N = int(input())    # 회의 개수
arr = list(map(int, input().split()))
meeting = []
for i in range(N):
    si, fi = arr[i*2], arr[i*2+1]
    meeting.append((si, fi))

# 종료시간 기준으로 오름차순 정렬
meeting.sort(key=lambda x:x[1])
print(meeting)