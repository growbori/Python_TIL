############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def check_email(user):

    # 여기에 코드를 작성하여 함수를 완성합니다.
    if '@' in user['email'] : # 만약 user['email'] 안에 '@'가 있다면
        answer = True # answer 는 True이고
    else: #아니라면
        answer = False # answer 는 False이다.
    return answer # answer 값 리턴하기



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
    'email': 'chibbo24@mail.com',
}
print(check_email(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(check_email(user_data2))  # False
#####################################################
