# number_of_people = 0

# def increase_user():
#     global number_of_people
#     number_of_people += 1

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# def create_user(name, age, address):
#     ()
#     user_info = {"name" : name, "age" : age, "address" : address}
#     print(f'{name}님 환영합니다!')
#     return user_info


many_user = None

info =  dict(zip(name, age))

def rental_book(info):

    print(f'{name}님이 {name // age}권의 책을 대여했습니다.')


number_of_book = 100

def decrease_book(number_of_book, rental_book):
    
    number_of_book = number_of_book - rental_book
    
    print(f'남은 책의 수 : {number_of_book}')



# user_list = list(map(create_user, name, age, address))

print(info)