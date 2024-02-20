def pre_order(T):
    if T:
        pre_order(left[T])
        pre_order(right[T])
        print(T, end=' ')       # 후위 순회 이므로 맨 마지막 print()

N = int(input())
E = N-1
arr = list(map(int, input().split()))
left = [0] * (N+1)
right = [0] * (N+1)
par = [0] * (N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0:
    c = par[c]

root = c
print(root)
pre_order(root)