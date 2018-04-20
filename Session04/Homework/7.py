class rectangle:
    length=1
    width=1
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        a=self.length*self.width
        return a

length=int(input("enter length"))
width=int(input("enter width"))
a1 = rectangle(length,width)

rec= a1.area()

print(rec)
