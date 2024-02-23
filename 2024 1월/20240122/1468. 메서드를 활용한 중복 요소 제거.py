# 아래 함수를 수정하시오.
def remove_duplicates(input):
    new_lst = []
    result = set(input)
    new_lst = list(result)

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
