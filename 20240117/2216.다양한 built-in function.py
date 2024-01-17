# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3

def change(negative):
    negative = abs(negative)
    return negative

result = change(negative)
print(result)

# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []

def test(empty_list):
    empty_list = bool(empty_list)
    return empty_list

result = test(empty_list)
print(result)

# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]

def summ(my_list):
    my_list = sum(my_list)

    return my_list
result = summ(my_list)
print(result)

# sum 함수를 사용해서 list 안의 값들을 다 더하자!
    

# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']

def sort_list(unsorted_list):
    unsorted_list.sort()
    return unsorted_list

result = sort_list(unsorted_list)
print(result)