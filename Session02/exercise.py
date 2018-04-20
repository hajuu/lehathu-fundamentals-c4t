# for i in range (2000,3201):
#     if i%7==0 and i%5!=0: #!= là khác
#         print(i,end=", ")

# ga=0
# tho=0
# for i in range(1,35):
#     if i*2+(35-i)*4==94:
#         print("ga",i)
#         print("tho",35-i)

# f=1
# n=int(input())
# for i in range(1,n+1):
#     f=f+100
# print(s)

n=int(input())
def tinhtong(n):
    if n==0:
        return 1
    else: return tinhtong(n+1)+100

#m=ord(1) mã ascii
#bài 12: import re or ascii




