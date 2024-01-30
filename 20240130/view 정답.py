'''

문제풀이 TIP!
answer = 0 조망권의 합 초기화

for i in range(2, n-3): 앞 뒤로 2칸은 빌딩이 존재하지 않으므로 조망권을 확인해야 하는 범위 줄어듬

i의 조망권 == 높이 H를 비교해서 나타낼 수 있음

조망권 높이 비교에 필요한 요소 [H-1], [H-2], [H+1], [H+2]

가장 높은 얘 보다 높아야 조망권 유지할 수 있음

4개중 가장 높은 얘 찾기 → if 문 사용 (원래는 max 사용해도 구할 수 있음)

max_v = 0 으로 초깃값을 설정해주고 문제 풀이 해도 무방

'''

T = 10 # 총 10개의 case에 대해 진행
for test_case in range(1, T+1): # 1-10까지의 범위 중 test_case
    cnt = 0 # 조망권이 확보되는 집의 개수 세기 위한 초기화
    N = int(input()) # 계산하고자 하는 총 건물의 수
    apt_list = list(map(int, input().split())) # 건물의 층수 정보를 list 형태로 받아오기

    for i in range(2, N-2): # 양쪽 맨 끝에 있는 2개는 원래 비어있으므로 굳이 범위 안에 넣어 줄 필요 없음
        if (apt_list[i] - apt_list[i+1] > 0) and (apt_list[i] - apt_list[i+2] > 0): # 만약 내가 구하고자 하는 i 번째 아파트의 높이가 i+1, i+2 보다 크다면
            if (apt_list[i] - apt_list[i-1] > 0) and (apt_list[i] - apt_list[i-2] > 0): # 만약 내가 구하고자 하는 i 번째 아파트의 높이가 i-1, i-2 보다 크다면
                cnt += (apt_list[i] - max(apt_list[i-1], apt_list[i-2], apt_list[i+1], apt_list[i+2])) # i 번째 아파트의 층수에서 나머지 4개의 층수 중 가장 큰 층수와의 차이를 구한다. 그리고 이런 높이 차 값들을 다 더해준다!
    
    print(f'#{test_case} {cnt}')
