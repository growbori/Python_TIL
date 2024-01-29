############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def tidy_up_company(email_list):
    Kemail = 0 # 'Koogle'에 해당하는 이메일의 갯수를 세는 함수
    Jemail = 0 # 'JCloud'에 해당하는 이메일의 갯수를 세는 함수
    Gemail = 0 # 'GaKao'에 해당하는 이메일의 갯수를 세는 함수
    Semail = 0 # 'School'에 해당하는 이메일의 갯수를 세는 함수
    Mmail = 0 # 'Maver'에 해당하는 이메일의 갯수를 세는 함수
    for i in range(len(email_list)): # 전체 이메일 리스트 길이를 범위로 주어주고 
        if email_list[i] == 'Koogle': # 만약 email_list안에 있는 i 번째 요소의 값이 'Koogle'과 같다면
            Kemail += 1 # Kemail에 값을 1 더해준다. 
        elif email_list[i] == 'Maver': # 만약 email_list안에 있는 i 번째 요소의 값이 'Maver'과 같다면
            Mmail += 1 # Mmail 값을 1 더해준다.
        elif email_list[i] == 'JCloud': # 이하동일하게 수행한다.
            Jemail += 1
        elif email_list[i] == 'GaKao':
            Gemail += 1

        elif email_list[i] == 'School':
            Semail += 1 # 여기까지 마치고 나면 각 이메일마다 email_list에 포함된 갯수들이 나타날 것이다. 
    
    email_summary = {} # 빈 딕셔너리 형태를 하나 만들어주고
    if 'Koogle' in email_list: # 만약 'Koogle'이 email_list 안에 있다면
        email_summary['Koogle'] = Kemail # 'koogle' 키 값의 value로 Kemail을 짝지어서 빈 딕셔너리에 넣어준다. 
    if 'JCloud' in email_list: # 만약 'JCloud'이 email_list 안에 있다면
        email_summary['JCloud'] = Jemail # 'JCloud' 키 값의 value로 Jemail을 짝지어서 빈 딕셔너리에 넣어준다. 
    if 'GaKao' in email_list: # 만약 'GaKao'이 email_list 안에 있다면
        email_summary['GaKao'] = Gemail # 'GaKao' 키 값의 value로 Gemail을 짝지어서 빈 딕셔너리에 넣어준다. 
    if 'School' in email_list: # 만약 'School'이 email_list 안에 있다면
        email_summary['School'] = Semail # 'School' 키 값의 value로 Semail을 짝지어서 빈 딕셔너리에 넣어준다. 
    if 'Maver' in email_list: # 만약 'Maver'이 email_list 안에 있다면
        email_summary['Maver'] = Mmail # 'Maver' 키 값의 value로 Mmail을 짝지어서 빈 딕셔너리에 넣어준다. 
    return email_summary # email_summary에 채워진 딕셔너리 값들을 확인한다.

    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
email_list1 = ['Koogle', 'Koogle', 'Maver']
print(tidy_up_company(email_list1))   # {'Koogle': 2, 'Maver': 1}

email_list2 = [
    'Koogle', 'Koogle', 'JCloud', 'Koogle', 'GaKao', 
    'School', 'Koogle', 'Maver', 'GaKao', 'Maver', 
    'Koogle', 'GaKao', 'School', 'GaKao', 'JCloud', 
    'School', 'GaKao', 'GaKao', 'Maver', 'Koogle'
]
print(tidy_up_company(email_list2))
# {'Koogle': 6, 'JCloud': 2, 'GaKao': 6, 'School': 3, 'Maver': 3}
#####################################################
