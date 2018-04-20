#class: quản lí code cho dễ

# class Tenclass:
    #thuộc tính -> biến variables
    #phương thức -> hàm con sub function

#Eg:
class hcn: #tên
    width=10 #gán mặc định
    height=100
    def __init__(self,w,h): #khởi tạo
        self.width=w
        self.height=h
    def chuvi(self): #bất kì hàm con nào đều có đầu vào là self,tham số cx self
        c = 2*(self.height+self.width)
        return c
#tạo
a1=hcn(10,100)
a2=hcn(30,100)

cv1=a1.chuvi()
print("chu vi a1: ",cv1)
cv2=a2.chuvi()
print("chu vi a2: ",cv2)

#questions on: class vì nó trừu tượng af
#class -> đối tượng
#class -> class -> object #object đc dùng thuộc tính của tất cả trc đó