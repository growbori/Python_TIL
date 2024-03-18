'''
숫자는 숫자끼리, 문자는 문자끼리 작성해서 두개를 합치는 문제 풀이방법!
'''

for tc in range(10):
    T = int(input())
    A = list(input())
    stack = []
    postfix = ''    # 후위표기법 생성할 빈 문자열
    for word in A:
        if word.isdigit():  # A 안에 들어있는 문자가 숫자이면
            postfix += word     # 후위표기법 안에 작성하기
        else:       # '+' 문자라면
            stack.append(word)      # stack 에다 쌓기!
    while stack:
        postfix += stack.pop()      # stack에 적힌 문자들을 뽑아와서 postfix에 작성
    # print(postfix)
    stack2 = []     # 후위표기법 완성한 postfix를 작성할 빈 스택
    for data in postfix:
        if data.isdigit():
            stack2.append(data)     # 후위표기법한 데이터를 스택에 쌓기!
        else:
            if len(stack2) >= 2:    # 만약 stack2의 길이가 2이상이면
                a = stack2.pop()    # 숫자들을 하나씩 빼오기!
                b = stack2.pop()
                if data == '+':
                    stack2.append(int(a)+int(b))    # a, b가 모두 문자열이므로 int형태로 바꾼 뒤 더한 값을 stack2에 표시!

    print(f'#{tc+1}', *stack2)



