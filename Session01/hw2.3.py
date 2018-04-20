#[3]
a=0
for i in range(1500,2701,1):
    if i%5==0 and i%7==0:
        a=a+1
        print(i)
print("no of no satisfied: ",a)