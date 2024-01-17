def create_user(name, age, address):
    # increase_user()
    #user_info = {}
    user_info = {'name' : '', 'age' : 0. 'address' : ''}
    print(user_info)
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다.')
    return user_info

result = create_user('홍길동', 30, '서울')

print(result)