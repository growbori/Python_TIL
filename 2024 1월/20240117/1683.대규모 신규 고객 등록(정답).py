number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {"name" : name, "age" : age, "address" : address}
    print(f'{name}님 환영합니다!')
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 함수에 여러개의 매개변수가 있을 경우, 
# map에 맨 앞에 함수명, 뒤에 차례대로 인자를 집어넣는 방식으로 구현한다.

user_list = list(map(create_user, name, age, address))
print(user_list)