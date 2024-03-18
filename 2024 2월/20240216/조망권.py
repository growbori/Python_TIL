'''
왼쪽과 오른쪽 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다.

조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
'''

for tc in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    answer = 0
    for i in range(2, len(height)-1):

        if (height[i] > height[i-1]) and (height[i] > height[i-2]):
            if (height[i] > height[i+1]) and (height[i] > height[i+2]):
                answer += height[i] - max(height[i-1], height[i-2], height[i+1], height[i+2])
    print(answer)