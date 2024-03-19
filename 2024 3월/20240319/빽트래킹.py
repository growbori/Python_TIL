'''
백트래킹

완전탐색 + 가지치기 완전탐색은 재귀를 활용

가능성이 없는(볼 필요가 없는) 경우의 수를 제거하는 방법

중복된 순열

1~3 까지 숫자 배열이 있을 때

111, 112, 113, 121,,,,,,,332, 333

재귀는 특점 시점으로 돌아오는게 핵심~!!!

파라미터는 바로 작성하지 않고

구조를 먼저 잡고, 구조에서 필요한 함수를 전역변수/변수로 활용
'''

arr = [i for i in range(1, 4)]
path = [0] * 3  # 뭘 선택했는지에 대한 정보 담기

def dfs(level):
    # 기저조건
    # 이 문제에서는 3개를 뽑았을 때 까지 반복

    if level == 3:  # level 이 3개가 되면 종료
        print(*path)
        return
    # 들어가기 전

    # 다음 재귀 호출
    # - 다음에 갈 수 있는 곳들은 어디인가?
    # - 이 문제에서는 1, 2, 3 세 가지(arr의 길이 만큼) 경우의 수가 존재
    # 기본 코드
    # path[level] = 1
    # dfs(level + 1)
    #
    # path[level] = 2
    # dfs(level + 1)
    #
    # path[level] = 3
    # dfs(level + 1)

    # for 문 활용
    for i in range(len(arr)):
        path[level] = arr[i]
        dfs(level+1)

    # 갔다 와서 할 로직

dfs(0)