flock=[5,7,300,90,24,50,75]
print("flock: ",flock)

for j in range(1,4):
    max=0
    for i in range(len(flock)):
        if flock[i]>max:
            max=flock[i]
    print("biggest sheep size: ",max)

    index=flock.index(max)
    default=8
    flock.remove(max)
    flock.insert(index,default)
    print("after shear biggest sheep, flock: ",flock)

    print()
    print("Month",j)
    flock[:]=(i+50 for i in flock) #dùng ngoặc vuông khác gì ngoặc tròn ????
    print("new flock:",flock)

print()
total=0
for i in range(len(flock)):
    total+=flock[i]
print("flock size:",total)
print("money:",total*2,"$")
