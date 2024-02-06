N = str(input())

count = 0
for i in range(int(N)+1):
    for j in range(60):
        for k in range(60):
            if N in str(i) + str(j) + str(k):
                count += 1

print(count)