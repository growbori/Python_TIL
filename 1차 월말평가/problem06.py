############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calc_total(cart_list):
    product_price = 0 # 전체 가격 초기화
    for product in cart_list: # cart_list 안에 있는 품목들 하나씩 불러오기
        if product == 'apple_pie': # 만약 cart 안에 있는 제품이 'apple_pie'라면
            product_price += item_dict['apple_pie'] # product_price에 'apple_pie'품목의 가격 더해주기
        elif product == 'banana_milk': # 만약 cart 안에 있는 제품이 'banana_milk'라면
            product_price += item_dict['banana_milk'] # product_price에 'banana_milk'품목의 가격 더해주기
        elif product == 'coconut_milk': # 이하동일하게 수행한다.
            product_price += item_dict['coconut_milk']
        elif product == 'egg_tart':
            product_price += item_dict['egg_tart']
        elif product == 'fruits_cocktail':
            product_price += item_dict['fruits_cocktail']    
        elif product == 'gum':
            product_price += item_dict['gum']
        elif product == 'hotdog':
            product_price += item_dict['hotdog']
        elif product == 'ice_cream':
            product_price += item_dict['ice_cream']
        elif product == 'juice':
            product_price += item_dict['juice']
        elif product == 'keyboard':
            product_price += item_dict['keyboard']
        elif product == 'lotion':
            product_price += item_dict['lotion']


    return product_price #최종으로 카트마다 합산된 제품의 총 가격 출력

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
item_dict= {
    'apple_pie': 2500,    'banana_milk': 1800,     'coconut_milk': 2000,
    'egg_tart': 2300,    'fruits_cocktail': 3000,    'gum': 1200,
    'hotdog': 2500,    'ice_cream': 3200,    'juice': 2800,
    'keyboard': 35000,  'lotion': 8700
}

cart1 = ['apple_pie', 'ice_cream', 'juice', 'gum', 'banana_milk']
print(calc_total(cart1))    # 11500
cart2 = ['coconut_milk', 'egg_tart', 'fruits_cocktail', 'lotion', 'keyboard']
print(calc_total(cart2))    # 51000
#####################################################
