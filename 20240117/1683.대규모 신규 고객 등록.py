number_of_people = 0


def increase_user(name, age, address):
    triple = zip(name, age, address)
    triple = list(triple)
    for i in range(len(triple)):
        print(f"'name' : {name[i]}, 'age' : {age[i]}, 'address' : {address[i]}")
    pass


def create_user(name):
    for i in range(len(name)):
        print(f'{name[i]}님 환영합니다!')
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

create_user(name)

result = increase_user(name, age, address)
