dex2hex = {'0': '0000',
           '1': '0001',
           '2': '0010',
           '3': '0011',
           '4': '0100',
           '5': '0101',
           '6': '0110',
           '7': '0111',
           '8': '1000',
           '9': '1001',
           'A': '1010',
           'B': '1011',
           'C': '1100',
           'D': '1101',
           'E': '1110',
           'F': '1111'
           }

T = int(input())
for tc in range(T):
    M, N = input().split()
    answer = []
    for i in range(len(N)):
        for k in dex2hex.keys():
            if N[i] == k:
                answer.append(dex2hex.get(k))

    print(f"#{tc+1} {''.join(answer)}")