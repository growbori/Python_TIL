number_of_people = 0

print(f'현재 가입 된 유저 수 : {number_of_people}')
def increase_user(number_of_people):
    
    number_of_people += 1
    print(f'현재 가입 된 유저 수 : {number_of_people}')



def create_user(name, age, address):
    print(f"{name}님 환영합니다!")
    pass
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(user_info)


create_user('홍길동', 30, '서울')
increase_user(number_of_people)
