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

# 순열
# 123, 132, 213, 231, 312, 321
# 조건 : 숫자는 한 번만 사용해라!

def dfs(level):

    if level == 3:  # level 이 3개가 되면 종료
        print(*path)
        return

    # 갈 수 있는 전체 후보군
    for i in range(len(arr)):
        # 여기는 못가!! (가지치기)
        # 백트래킹 코드 팁
        # 갈 수 없는 경우를 활용
        # 아래 코드처럼 갈 수 없을 때 Continue
        # if arr[i] not in path:
        #     path[level] = arr[i]
        #     dfs(level+1)
        if arr[i] in path:
            continue

        path[level] = arr[i]
        dfs(level + 1)

        # 갔다 와서 할 로직
        # 기존 방문을 초기화 해주어야 함
        path[level] = 0

dfs(0)