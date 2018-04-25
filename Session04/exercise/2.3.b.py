for i in range(8):
    print (1,0, end=" ")
print()
n=int(input("enter n: "))
if n%2==0:
    for i in range(n//2):
        print(1,0,end=" ")
else:
    n=n//2
    for i in range(n):
        print(1,0,end=" ")
    print(1)