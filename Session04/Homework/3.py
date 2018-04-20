def k_mer(string,k):
    count={}
    n=len(string)
    for i in range(0,n-k+1):
        kmers=string[i:i+k]
        if kmers not in count:
            count[kmers]=0
        count[kmers]+=1
    return count
string=input("Enter string: ")
k=int(input("Enter k: "))
print(k_mer(string,k))

