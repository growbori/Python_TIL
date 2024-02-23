data = [
    {
        'name': 'galaxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galaxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galaxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

for i in range(len(data)):
    print(f'name은/는 {data[i]["name"]}입니다.')
    print(f"company은/는 {data[i].get('company', 'unknown')}입니다.")
    print(f'is_collapsible은/는 {data[i]["is_collapsible"]}입니다.')



