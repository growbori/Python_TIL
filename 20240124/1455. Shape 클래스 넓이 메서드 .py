# 아래 클래스를 수정하시오.
class Shape:
    pass
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        area1 =  self.width * self.height
        return area1
    
shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)
