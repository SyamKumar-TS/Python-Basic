n=int(input("enter number:"))
sum=0
while n>0:
    num=n%10
    sum=sum+num
    n=n//10
print(sum)    