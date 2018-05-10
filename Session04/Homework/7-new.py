class Rectangle:
    def __init__(self):
        self.width=int(input("enter width: "))
        self.height=int(input("enter height: "))
    def area(self):
        print(self.height*self.width)

a=Rectangle()
a.area()