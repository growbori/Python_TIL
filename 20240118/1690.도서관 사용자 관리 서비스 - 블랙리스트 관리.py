import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
response = requests.get(API_URL)

parsed_data = response.json()

dummy_data = []


for i in range(1, len(parsed_data)):

    if float(parsed_data[i]['address']['geo']['lat']) < 80 and float(parsed_data[i]['address']['geo']['lng']) > -80:
        dummy_data.append({'company' : parsed_data[i]['company']['name'], 'lat' : parsed_data[i]['address']['geo']['lat'], 'lng' : parsed_data[i]['address']['geo']['lng'], 'name' : parsed_data[i]['name']})

# print(dummy_data)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(dummy_data):
    for i in range(len(dummy_data)):
        key = dummy_data[i]['company']
        value = dummy_data[i]['name']
        censored_user_list = {key : [value]}
        print(censored_user_list)
        return censored_user_list
    pass

# create_user(dummy_data)

def censorship(create_user):
    
    for i in range(len(dummy_data)):
        key = dummy_data[i]['company']
        value = dummy_data[i]['name']
        if key in black_list:
            print(f'{key} 소속의 {value} 은/는 등록할 수 없습니다.')

        else:
            print('이상 없습니다.')

    pass

censorship(create_user)



