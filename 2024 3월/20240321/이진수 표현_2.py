T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
 
    if M&((1<<N)-1) == ((1<<N)-1):
        answer = 'ON'
    else:
        answer = 'OFF'
 
    print(f'#{tc+1} {answer}')