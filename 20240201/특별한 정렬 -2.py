T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 정수 개수
    numbers = list(map(int, input().split())) # 리스트 형태로 숫자들을 받아오고

    result = list() # 빈 리스트 생성
    while numbers: # numbers 리스트 안에 숫자가 있는 동안,
        max_number = numbers[0] # 가장 큰 숫자를 numbers[0] 이라고 가정
        min_number = numbers[0] # 가장 작은 숫자를 numbers[0] 이라고 가정
        for number in numbers: # numbers 안에 있는 number에서
            if number > max_number: # 만약 숫자가 기존에 있던 가장 큰 숫자보다 크다면
                max_number = number # 가장 큰 숫자가 갱신된다.
        for number in numbers:
            if number < min_number: # 만약 숫자가 기존에 있던 가장 작은 숫자보다 작으면
                min_number = number # 가장 작은 숫자가 갱신된다.
        result.append(max_number) #이렇게 출력된 ex. 10을 result 결괏값에 append 해준다.
        result.append(min_number) #이렇게 출력된 ex. 1을 result 결괏값에 append 해준다.

        numbers.remove(max_number) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 에서 이미 최댓값 10을 구해서 result에 작성했으므로 10 숫자를 제외한다.
        numbers.remove(min_number) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 에서 이미 최솟값 1을 구해서 result에 작성했으므로 10 숫자를 제외한다.

# 이렇게 계속 반복하다보면 맨 끝에 있는 최댓값, 최솟값이 result에 가서 적히게 된다!
    print(f'#{test_case}', *result[:10] , end='\n')
    # print(*result[:10])
    
# 테스트 케이스가 짝수여야 함! 홀수일 경우 case를 2개로 나눠서 계산해야 함!