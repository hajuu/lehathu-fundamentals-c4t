# x=10
# while x!=5: #stop at 5
#     x=x-1
#     if x%2!=0: continue
#     print(x)

#while đk: đk chủ yếu so sánh
#operation in python

#dictionary: key(ko thay đổi)+data(thay đổi)
# lop_c4t={"tenlop":"c4t","siso":15} #key:data
# print(lop_c4t) #print dict
# print(lop_c4t["tenlop"])
#
# print(lop_c4t.keys())
# print(lop_c4t.values())
#
# lop_c4t["tenlop"]="hello" #change data
# print(lop_c4t)
# print(lop_c4t["siso"]) #print data

#lop_c4t={"tenlop":"c4t","siso":(15,29,"danhsachlop"} ==> print "siso": (15,29...)


#cách tạo bảng
a=dict() #or a={} to create a dict
# a["name"]="bien"
# print(a)
# a["name"]="hello"
# print(a)
#
a[1]=100 #assign key+value
print(a)

#baitap3
# n=int(input())
# a={} #dict create trước
# for i in range(1,n+1):
#     a[i]=i*i #assign value
# print(a, end=" ")

#tuple: immutable/ko thể thay đổi
#tuple mở rộng được
#sinh ra tuple: biến local, global; có thể hiểu là const
#eg
# a=(1,2,3)
# b=(1,2)
# print(hex(id(a))) #có 1 địa chỉ bộ nhớ của biến, địa chỉ a0
# a=a+b
# print(a)
# print(hex(id(a))) #địa chỉ a1 -> biến khác nhau
#
# print("array") #về tuple
# c=[1,2,3] #ngoặc vuông obviously là tuple?
# print(hex(id(c))) #địa chỉ c0
# c.append([1,2])
# print(c)
# print(hex(id(c))) #vẫn địa chỉ c0, ko thay đổi

#có thể từ id tìm ra tuple
#buổi sau: class; cơ bản hết python
#thứ 6 cn tuần sau nghỉ
#học cấu trúc: sơ đồ vòng lặp
