for i in range(10):
   for j in range(10):
       if (i+j)%2==0:
           print(1, end=" ")
       else: print (0, end=" ")
   print()
print()
n=int(input("enter n: "))
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print(1,end=" ")
        else: print(0,end=" ")
    print()