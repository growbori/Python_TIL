'''
10*10 격자에 빨간색과 파란색을 칠하려고 한다.
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후
보라색이 된 칸 수를 구하는 프로그램을 구하시오
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split()))]