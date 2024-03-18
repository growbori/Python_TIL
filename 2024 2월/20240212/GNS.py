T = int(input())

for _ in range(T):
    tc, N = input().split()
    numlist = input().split()
    count = [0] * 10
    language = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in numlist:
        for j in range(10):
            if i == language[j]:
                count[j]+=1
                break
    print(tc)
    for i in range(10):
        print(f'{language[i]} '*count[i], end = ' ')
    print()