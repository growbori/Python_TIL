def restructure_word(word, arr):
    pass

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

arr.extend(original_word)
print(arr)

def restructure_word(word):

    for i in word:
        cnt = 0
        if i.isdecimal() == True:
            while cnt < int(i):
                cnt += 1
                arr.pop()

        else:
            arr.remove(i)
    print(arr)

    print(''.join(arr))



result = restructure_word(word)
