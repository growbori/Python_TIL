# 아래 함수를 수정하시오.
def find_min_max(input):
    
    input.sort()
    a = input[0]
    b = input[4]
    answer = a, b
    
    return tuple(answer)

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
