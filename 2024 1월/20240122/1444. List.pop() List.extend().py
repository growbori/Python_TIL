# 아래 함수를 수정하시오.
# solution 1
# def even_elements(input):
    
#     for i in input:
#         if i % 2 != 0:
#             input.remove(i)
    
#     return input


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)


# solution 2

# def even_elements(input): 

#     for i in input:
#         if i % 2 != 0:
#             my_list.pop(input.index(i))
    
#     return my_list


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)

# solution 3

def even_elements(num_list): 

    result_list = []

    while num_list: # num_list 의 길이가 존재하는 한
        r = num_list.pop(0)
        if r % 2 == 0:
            result_list.extend([r])
    return result_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)