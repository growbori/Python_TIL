T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    fire = []
    front, rear = -1, N-1
    for i in Ci:
        fire.append(i)  # 화덕에 피자 넣기
        Ci.pop(0)       # 대기 화덕 피자 리스트
        if len(fire) == N:
            break
    print(fire)
    for i in range(M):
        i = i % M
        if i == 0 and fire[i] == 0:     # 맨 앞에 있는 피자가 완성되었으면
            fire.pop(0)     # 화덕에서 피자를 빼고
            if len(Ci) >= 1:       # 대기 화덕에 피자가 있으면
                fire.append(Ci[0])     # 대기 화덕에 있던 친구 데려오기!
            else:
                continue
        elif i == 0 and fire[i] != 0:   # 맨 앞에 있는 피자이지만 완성되지 않았으면
            fire[i] = fire[i] // 2      # 피자위의 치즈 양을 반으로 줄이고
            fire.append(fire[0])        # 처음 나온 값을 붙이고
            fire.pop(0)
    print(fire)


