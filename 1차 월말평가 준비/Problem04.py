############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def turn(temperature_list):
    maximum = []
    minimum = []

    for i in range(len(temperature_list)):
        if temperatures1[i][0] > temperatures1[i][1]:
            maximum.append(temperatures1[i][0])
            minimum.append(temperatures1[i][1])
            i += 1
        else:
            maximum.append(temperatures1[i][1])
            minimum.append(temperatures1[i][0])
            i += 1
    
    dictionary = {}

    dictionary['maximum'] = maximum
    dictionary['minimum'] = minimum

    return dictionary

    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
temperatures1 = [
    [9, 3],
    [9, 0],
    [11, -3],
    [11, 1],
    [8, -3],
    [7, -3],
    [-4, -12]
]
print(turn(temperatures1)) 
# {'maximum': [9, 9, 11, 11, 8, 7, -4], 'minimum': [3, 0, -3, 1, -3, -3, -12]}
#####################################################