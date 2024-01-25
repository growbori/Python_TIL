# 아래에 코드를 작성하시오.

class Myth:
    count = 0
    def __init__(self, name):
        self.name = name
        Myth.count += 1

    @staticmethod
    def staticmethod(story):
        return story

story = '신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.'
Myth1 = Myth('dangun')
Myth2 = Myth('greek & rome')
print(Myth1.name)
print(Myth2.name)
print(Myth.count)

Myth3 = Myth.staticmethod(story)
print(Myth3)



