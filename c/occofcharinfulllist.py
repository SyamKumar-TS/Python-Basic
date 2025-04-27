lst=list(map(str,input("enter elements:").split()))
count=0
c=input("enter char:")
for i in lst:
    for j in i:
        if j==c:
            count += 1
print(count)