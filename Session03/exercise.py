#bài 6
# X=3
# Y=5
# b=[]
# for i in range(X):
#     a=[]                   #line 2,3,4->tạo mảng 1 chiều
#     for j in range(Y):
#         a.append(i*j)
#     b.append(a) #tạo ra nhiều hàng
# print(b)

#số ptu trong mảng 1 chiều là số cột
#tạo ra mảng 2d tạo 2 vòng for

a=[7,5,3,10] # print(a[1])->5 lmao
x = a.copy()
b=[]
ind=0
c=[]
while len(a)>0:
    lowest=100000
    for i in range(len(a)):
        if a[i]<lowest:
            lowest=a[i]
            inda = i
    indx = 0
    for j in range(len(x)):
        if lowest == x[j]:
            indx = j
    c.append(indx)
    b.append(lowest)
    a.remove(a[inda])
    # if len(a)>0:
    #     lowest=a[0]
print(b)
print(c)

#7
a=input("type in words")
b=[]
c=a.split(",")
chiso=0
d=[] #tạo mảng chữ cái đầu tiên theo ascii
e=[]
for i in c:
    first=ord(i[0])
    d.append(first)
print(d)
lowest=d[0]
while len(d)>0:
    for j in range(len(d)):
        if d[j]<lowest:
            lowest=d[j]
            chiso=j
        e.append(chiso)
    b.append(lowest)
    d.remove(d[j])
    if len(d)>0:
        lowest=d[0]
print(b,e)




