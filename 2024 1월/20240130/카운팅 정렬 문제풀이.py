N = 6

K = 9

data = [7, 2, 4, 5, 2, 3] # 0~9, K = 9

counts = [0] * (K + 1) # 0~9 사이의 값들이 있는지 확인하는 범위를 생성하는 것 이므로 크기가 K+1 인 빈 리스트 생성하기
 
temp = [0] * N # 누적합의 정렬된 결과를 넣을 빈 리스트
# counts 배열에 기록하기

for x in data: # data 안에 있는 값들의 갯수를 세서 count 빈 리스트에 넣어주기
    counts[x] += 1

# counts 누적합 구하기
    
for i in range(1, K + 1): # 1부터 K번 인덱스까지 (위에서 counts의 범위를 K+1 까지로 했으므로 동일하게 범위 지정)
    counts[i] = counts[i-1] + counts[i] # 누적합 구하기

# data의 마지막 원소부터 정렬하기

for i in range(N-1, -1, -1) : #N-1부터 0번째까지 감소하는 형태로 더해주기
    counts[data[i]] -= 1 # 인덱스 위치를나타내기 위해선 count의 시작이 0부터 이므로 -1을 해줘야 한다. (남은 개수 계산)
    temp[counts[data[i]]] = data[i] # counts[data[i]] 에 해당하는 temp 값에 data[i]를 대입한다.
print(*temp)