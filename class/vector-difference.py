class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def difference(self):
        print(f"Разность векторов равна: ({self.x1-self.x2}, {self.y1-self.y2})")
vector = Vector(3, 3, 4, 4)
vector.difference() 