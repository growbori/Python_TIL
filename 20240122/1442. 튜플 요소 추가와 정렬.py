# 아래 함수를 수정하시오.
def sort_tuple(input):
    new_tuple = ()
    new_tuple = list(input)
    new_tuple.sort()
    new_tuple = tuple(new_tuple)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
