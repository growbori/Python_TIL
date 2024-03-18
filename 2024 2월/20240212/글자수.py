T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    max_count = 0

    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1
                if max_count < count:
                    max_count = count
    print(max_count)