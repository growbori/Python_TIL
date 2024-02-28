'''
.......... 로 된 1차원 초원에 공은 '()'이렇게 표현되며 서로 다른 두 공이 겹치지 않는다.
|..().()|||. 이렇게 잡초가 자라서 몇개의 칸이 가려졌다.
초원에 놓을 수 있는 최소 공의 개수를 구하여라
'''

T = int(input())
for tc in range(T):
    yard= input()

    a = yard.count('(|')
    b = yard.count('|)')
    c = yard.count('()')

    # count = 0
    # if ('(|' or '|)' or '()') in yard:
    #     count += 1

    print(f'#{tc+1} {a+b+c}')