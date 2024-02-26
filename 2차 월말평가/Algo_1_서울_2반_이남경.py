
'''
N개의 칸에 돌이 한 개씩 들어있다.
M 번의 뒤집기를 진행하는데, 뒤집기는 3가지 작업 방식이 있다.
1번 작업은 i번째 부터 j개의 돌을 뒤집는다.
2번 작업은 i번째 부터 j개의 돌을 i번째 돌의 색으로 바꿔놓는다.
3번 작업은 i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
'''
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))     # 첫번째 인덱스 자리가 0이므로 앞에 빈 칸을 넣어줘서 인덱스 값을 조정해준다.
    for _ in range(M):
        i, j, w = map(int, input().split())     # i 기준 위치, j 작업할 돌의 수, w 작업 번호

        for x in range(N):  # 전체 N 동안
            count = 0   # 시행 횟수 세기
            if count == M:  # 시행 횟수가 M과 같으면
                break       # 멈춘다!
            else:   # 시행 횟수가 다 차지 않았다면
                if i > 0 and (i + j) <= N:
                    if w == 1:      # w == 1이라면
                        for y in range(i, i + j):   # i 번째부터 j 번째 돌을 뒤집는다.
                            if arr[y] == 0:     # 기존에 있던 돌이 0이면
                                arr[y] = 1      # 1로 바꿔주고
                            else:       # 기존에 있던 돌이 1이면
                                arr[y] = 0  # 0으로 바꿔준다.
                        count += 1      # 1회 시행되었으므로 count 에 1을 올려준다.
                    if w == 2:      # w == 2라면
                        for y in range(i, i + j):       # i 번째부터 j개의 돌을 i번째 돌의 색으로 바꿔놓는다.
                            if arr[i] == 0:
                                arr[y] = 0
                            else:
                                arr[y] = 1
                        count += 1
                if 0 <= (i-j) and (i+j) <= N:
                    if w == 3:      # w == 3이면
                        for y in range(i): # i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해
                            for t in range(0, j):
                                if arr[y - t] == 0 and arr[y+t] == 0 :  # 같은 색이면 뒤집는다.
                                    arr[y-t] = 1
                                    arr[y+t] = 1
                                if arr[y-t] == 1 and arr[y+t] == 1: # 같은 색이면 뒤집는다.
                                    arr[y-t] = 0
                                    arr[y+t] = 0
                                else:   # 다른 색이라면 그냥 냅둔다.
                                    continue
                        count += 1
    print(f'#{tc+1}', *arr[1:])