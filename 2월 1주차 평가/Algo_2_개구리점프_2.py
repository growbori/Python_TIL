"""
김싸피는 어느날 개구리 꿈을 꾸었다. 개구리는 호수 위 N개의 연잎에서 뛰고
있었는데, 연잎에는 숫자가 쓰여 있었다. 김싸피는 개구리가 어떤 규칙으로
점프하고 있다는 것을 알았다. 개구리가 K 번 점프했을 때 개구리가 밟은
연잎의 모든 숫자의 합은 몇인가?
[규칙]
- 개구리가 점프를 시작하는 위치는 항상 제일 왼쪽이다. 시작시에 밟고 있는
연잎의 숫자는 결과에 더하지 않는다.
- 연잎의 숫자가 양수인 경우 앞(왼쪽에서 오른쪽으로)으로 점프한다.
- 연잎의 숫자가 음수인 경우 뒤(오른쪽에서 왼쪽으로)로 점프한다.
- 한 번 뒤로 갔다가 다시 앞으로 뛸 경우에는 직전에 뒤로 간 칸만큼 더 앞으로
점프한다. (직전 움직인 거리가 -1이고, 현재 연잎 숫자가 2라면 다음 점프에서
앞으로 3칸 간다. 연속으로 두 번 이상 뒤로 간 경우 마지막 뒤로 간 거리만큼만
앞으로 간다.)
- 연잎 범위를 벗어나는 경우 호수에 빠져 더 이상 점프 하지 않는다.
위 그림과 같은 예시에서 개구리가 4번 점프한다면,
- 첫 번째 점프: 개구리는 앞으로 두 칸 뛰어 -2를 밟아서 누적합은 -2
- 두 번째 점프 : 개구리는 뒤로 두 칸 뛰어 2를 밟아서 누적합은 0
- 세 번째 점프 : 개구리는 앞으로 네 칸 뛰어(2+2) 1을 밟아 누적합은 1
- 네 번째 점프 : 개구리는 앞으로 한 칸 뛰어 1을 밟아 누적합은 2
이므로 개구리가 4번 점프했을 때 개구리가 밟은 연잎 숫자의 총합은 2이다.
입력
첫 줄에 테스트 케이스 개수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 N, K가 주어진다.
다음 N줄에 각 N개의 정수 Ai가 띄어쓰기로 구분되어 주어진다.
(1 <= N <= 10, 1 <= K = 10) , ( 1<= | Ai |<= 5 )
출력
각 줄에 테스트케이스 번호를 #번호 형태로 출력하고, 한 칸 띄워 개구리가
밟은 숫자의 합을 출력한다.
"""
t = int(input())

for test_case in range(1, t + 1):
    N, K = map(int, input().split())
    leaf = list(map(int, input().split()))

    current = 0   # 현재 위치를 저장해 줄 변수
    jump_count = 0    # 점프 횟수를 저장해 줄 변수
    current_index = 0
    leaf_sum = 0
    back_count = 0
    back_num = 0

    while jump_count < K:   # 점프를 k번 하기 전까지 실행
        try:
            if leaf[current_index] > 0:   # 현재 연잎의 숫자가 0보다 클 때
                if back_count != 0:   # 저번 시행에 back 했을 때
                    current_index += abs(back_num) + leaf[current_index]    # 현재 인덱스 저번 시행 수 + 현재 인덱스 만큼 이동
                    leaf_sum += leaf[current_index]
                    back_count = 0   # back_count 초기화
                else:
                    current_index += leaf[current_index]  # 현재의 인덱스 값을 그 숫자만큼 이동
                    leaf_sum += leaf[current_index]  # 리프의 숫자 합을 그 숫자만큼 더해줌

            elif leaf[current_index] < 0:   # 현재 연잎의 숫자가 0보다 작을 때
                current_index -= leaf[current_index]   # 인덱스를 뒤로 이동동
                leaf_sum += leaf[current_index]   # 리프의 숫자 합을 그 숫자만큼 더해줌
                back_count += 1   # 뒤로 갔는지 여부 확인
                back_num = leaf[current_index]   # 뒤로 갔을 때 숫자 저장

            jump_count += 1   # 점프 한 번 시행

        except IndexError:
            break

    print(f'#{test_case} {leaf_sum}')