############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def compare_pw(user):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    count = 0 # 문자열의 길이를 더하기 위해서 count로 초기화 해줌
    for _ in user['password']: # user['password'] 안의 값들 중
        if 'q' in user['password']: # 만약 user['password'] 안에 'q'가 있으면
            count += 1 # count 에 1을 더해준다.
        elif '1' in user['password']: # 만약 user['password'] 안에 '1'가 있으면
            count += 1 # count 에 1을 더해준다.
        elif 'w' in user['password']: # 이하동일하게 수행한다.
            count += 1
        elif '2' in user['password']:
            count += 1
        elif 'e' in user['password']:
            count += 1
        elif '3' in user['password']:
            count += 1
        elif 'r' in user['password']:
            count += 1
        elif '4' in user['password']:
            count += 1  # 여기까지 하고 나면 전체 문자열의 갯수가 구해질 것이다. 

    if 8 <= count < 32 and user['password'] == user['password_confirm']: # 만약 count 한 문자열의 길이가 8이상 32미만이고 user['password']가 user['password_confirm'] 랑 동일하다면
        answer = True # answer 는 True 이고
    else: # 조건이 만족하지 않는다면 
        answer = False # answer 는 False 이다. 
    
    return answer    # answer 값을 리턴해준다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'goodjob24@mail.com',
}
print(compare_pw(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(compare_pw(user_data2))  # False
#####################################################
