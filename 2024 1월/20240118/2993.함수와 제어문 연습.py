food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

for i in range(len(food_list)):
    key = food_list[i]['종류']
    value = food_list[i]['이름']
    if value == '토마토':
        food_list[1]['종류'] = '과일'
        print(f'{value} 은/는 과일 (이)다.')
    elif value == '자장면':
        print(f'{value}엔 고춧가루지')
        print(f'{value} 은/는 {key} (이)다.')
    else:
        print(f'{value} 은/는 {key} (이)다.')

    


print(food_list)

