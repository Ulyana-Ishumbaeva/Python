class Length:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def len(self):
        print(f"Длина вектра равна: {(self.x**2 + self.y**2)**0.5}")
vector = Length(4,3)
vector.len()