list=list(map(int,input("enter elements:").split()))
num=list[0]
for i in range(1,len(list)):
  
        if list[i]>list[0]:
            num=list[i]
print(num)            