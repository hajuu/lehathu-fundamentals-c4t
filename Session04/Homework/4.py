list=[(1,2,40),(0,15,60),(10,80,0)]

list1=[]
for i in list:
    list1.append(i[:-1]+(100,))
print(list1)
