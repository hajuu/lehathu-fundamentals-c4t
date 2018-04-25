for i in range(10):
    if i%2==0:
        i=1
    else:
        i=0
    for j in range(10):
        if j%2==0:
            j=1
        else:
            j=0
        print(i*j,end=" ")
    print()