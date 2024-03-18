n = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 매 시간 안에 'n'이 포함되어 있으면 카운트 증가
            if str(n) in str(i) + str(j) + str(k):
                count += 1

print(count)

'''
5
'''