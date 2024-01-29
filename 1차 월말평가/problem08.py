############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list):
    for i in range(len(number_list)): # num_list 의 길이 범위 사이에 미지수 i를 지정
        if number_list[i] not in number_list[i+1:]: # 만약 number_list[i] 가 number_list[i+1] 보다 큰 범위 안에 존재하지 않으면 (중복이 없으면)
            answer = number_list[i] # answer 는 number_list[i] 이다.
        else : # 아니라면
            continue # 중복값이 존재하는 경우이므로 무시하고 지나간다.
        
        return answer  #answer를 리턴 해준다. 

    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################
