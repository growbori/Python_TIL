# def KFC(x):
#     if x == 6:
#         return
#
#     print(x, end = ' ')
#     KFC(x+1)
#     print(x, end = ' ')

# branch = 2
# level = 3
#
# def run(level):
#     if level == 3:
#         return
#
#     for i in range(2):
#         run(level + 1)
#
# run(0)

# path = []
#
# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#
# KFC(0)
# print()

# 중복 순열
path = []

def Type_1(x, sum):

    if sum > 10:        # 가지치기 불필요한 과정 제거! 런 타임 줄일 수 있음
        return
    if x == 3:
        if sum <= 10:
            print(f'{path} = {sum}')    # 출력
        return

    for i in range(1, 7):
        path.append(i)
        Type_1(x+1, sum + i)
        path.pop()

Type_1(0, 0)
print()

# # 순열
# path = []
# used = [False for _ in range(7)]
# def Type_2(x):
#     if x == N:  # level의 갯수
#         print(path)
#         return
#
#     for i in range(1, 7):   # 구하고자 하는 숫자의 범위
#         if used[i] == True : continue
#         used[i] = True
#         path.append(i)
#         Type_2(x+1)
#         path.pop()
#         used[i] = False
#
# # Type_2(0)
# # print()
#
# N, Type = map(int, input().split())
# if Type == 1:
#     Type_1(0)
# else:
#     Type_2(0)
#
# print()
