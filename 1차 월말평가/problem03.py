############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def check_user_id(user):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    count = 0 # 문자열 갯수 합을 담을 count 함수 초기화
    for _ in user['user_id']: # user딕셔너리 안의 값 중 'user_id'에서 
        if 'l' in user['user_id']: # 만약 user['user_id'] 안에 'l'이 있다면
            count += 1 # 카운트를 하나 더해준다. 
        elif 'e' in user['user_id']: # 만약 user['user_id'] 안에 'e'이 있다면
            count += 1 # 카운트를 하나 더해준다. 
        elif 's' in user['user_id']: # 이하동일하게 수행
            count += 1
        elif 'a' in user['user_id']:
            count += 1
        elif 'f' in user['user_id']:
            count += 1
        elif 'y' in user['user_id']:
            count += 1
        elif '2' in user['user_id']:
            count += 1
        elif '4' in user['user_id']:
            count += 1
        elif 'e' in user['user_id']:
            count += 1
        elif 'd' in user['user_id']:
            count += 1
        elif 'u' in user['user_id']:
            count += 1
    if 4 <= count < 16: # 만약 문자열의 총 길이가 4이상 16 미만이라면
        answer = True # answer는 True이고
    else: # 아니라면
        answer = False # answer는 False 이다.
    return answer  # 리턴된 answer의 값을 작성해준다.


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
print(check_user_id(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(check_user_id(user_data2))  # False
#####################################################
