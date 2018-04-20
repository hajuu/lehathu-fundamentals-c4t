#[2]
a=[1,2,3,4,5,6,7,8,9]
odd=0
even=0
for i in a:
    if i%2==1: odd=1+odd
    else: even=1+even
print("no of odd no: ",odd)
print("no of even no: ",even)