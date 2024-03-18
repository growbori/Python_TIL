T = int(input())

for tc in range(T):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    print(nums[-1] - nums[0])