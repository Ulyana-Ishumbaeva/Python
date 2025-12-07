class K:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def coeff(self):
        print(f"Угловой коэфициент равен: {(self.y2 - self.y1)/(self.x2-self.x1)}")
vector = K(3,2,4,5)
vector.coeff()