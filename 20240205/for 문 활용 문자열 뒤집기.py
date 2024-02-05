A = ['a', 'b', 'c', 'd', 'e']
N = len(A)
for i in range(N//2+1):
    A[i], A[N-1-i] = A[N-1-i], A[i]

print(A)