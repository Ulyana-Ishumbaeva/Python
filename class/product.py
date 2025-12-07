class Vector_product:
    def __init__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def prod(self):
        print(f"Скалярное произведение векторов равно: {self.x1*self.x2 + self.y1*self.y2}")
vectors = Vector_product(3,3,4,4)
vectors.prod()