# 아래 클래스를 수정하시오.
class StringRepeater:
    
    def repeat_string(self, mul, word):
        self.mul = mul
        self.word = word
        repeater1 = self.mul * (self.word +'\n')
        return repeater1



repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
print(repeater1.repeat_string(3, "Hello"))