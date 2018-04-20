class car:
    brand="audi"
    maxspeed=200

    def setBrand(self,b):
        self.brand=b

    def setMaxSpeed(self,s):
        self.maxspeed=s

    def printData(self):
        print(self.brand, "car with maxSpeed", self.maxspeed)

brand=input("enter brand: ")
maxspeed=int(input("enter maxspeed: "))
c1=car()
c1.setBrand(brand)
c1.setMaxSpeed(maxspeed)
c1.printData()