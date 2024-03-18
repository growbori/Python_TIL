T = int(input())
for tc in range(1, T + 1):
    tn, list_length = input().split()
    list_length = int(list_length)
    alien_number_str = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    number_list = list(input().split())
    number_list.sort(key = lambda x : alien_number_str.index(x))
    print(f'#{tc}')
    print(*number_list)