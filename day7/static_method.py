class math: 
    def __init__(self, num):
        self.num = num
    def addtwonum(self, n): 
        self.num = self.num +n 
    @staticmethod 
    def add(a, b): 
        return a+ b
a = math(5)
print(a.num)
a.addtwonum(9)

