# 아래 함수를 수정하시오.
def difference_sets(set1, set2):
    answer = set1.difference(set2)
    return answer

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)