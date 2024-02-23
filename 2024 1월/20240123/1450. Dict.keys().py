# 아래 함수를 수정하시오.
def get_keys_from_dict(my_dict):
    result = []
    for key in my_dict.keys():
        result.append(key)
    return result


    

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']