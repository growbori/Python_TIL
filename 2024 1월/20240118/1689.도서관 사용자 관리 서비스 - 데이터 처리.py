import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
# print(response)

# 변환 데이터 출력
# print(parsed_data)
# 변환 데이터의 타입
# print(type(parsed_data))
dummy_data = []
# 특정 데이터 출력

for i in range(1, len(parsed_data)):

    parsed_data[i]['company']['name']
    parsed_data[i]['address']['geo']['lat']
    parsed_data[i]['address']['geo']['lng']
    parsed_data[i]['name']

    if float(parsed_data[i]['address']['geo']['lat']) < 80 and float(parsed_data[i]['address']['geo']['lng']) > -80:
        dummy_data.append({'company' : parsed_data[i]['company']['name'], 'lat' : parsed_data[i]['address']['geo']['lat'], 'lng' : parsed_data[i]['address']['geo']['lng'], 'name' : parsed_data[i]['name']})

print(dummy_data)
