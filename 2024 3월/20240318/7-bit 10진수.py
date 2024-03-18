# 70 자리 2진수를 앞에서부터 7비트씩 잘라 10진시룰 출력하시오

T = int(input())
for tc in range(T):
    arr = list(input())
    number = 0
    numList = []
    for i in range(10):
        bit = arr[7*i:7*(i+1)]
        # print(bit)
        bit.reverse()
        for i in range(len(bit)):
            number += int(bit[i]) * 2**int(i)

        numList.append(number)
    numList = [0] + numList
    # print(numList)
    print(f'#{tc+1}', end = ' ')
    for i in range(len(numList)-1):
        print(numList[i+1]-numList[i], end = ' ')
    print()
