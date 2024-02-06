def use_B(A, B):
    count = 0
    i = 0
    while i < len(A) - len(B) + 1:
        if A[i] == B[0]:
            for j in range(len(B)):
                if A[i + j] != B[j]:
                    i += 1
                    break
            else:
                count += 1
                i += len(B)
        else:
            i += 1
    return count


T = int(input())
for tc in range(1, 1 + T):
    A, B = input().split()  # A는 타이핑해야되는 거, B는 저장되어있는 녀석
    use_B(A, B)
    print(f'#{tc} {len(A) - use_B(A, B) * (len(B) - 1)}')