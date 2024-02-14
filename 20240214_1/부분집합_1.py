bit = [0, 0, 0, 0]

for i in range(2):  #0, 1 중 하나의 숫자를 bit[0]에 대입
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)     # 0, 1을 대입해서 나올 수 있는 모든 경우의 수를 구함