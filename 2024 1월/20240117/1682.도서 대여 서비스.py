

def rental_book(name, rental_book):
    print(f'{name}님이 {rental_book}권의 책을 대여했습니다.')
    pass

number_of_book = 100

def decrease_book(number_of_book, rental_book):
    
    number_of_book = number_of_book - rental_book
    
    print(f'남은 책의 수 : {number_of_book}')
    pass

decrease_book(number_of_book, 3)
rental_book('홍길동', 3)