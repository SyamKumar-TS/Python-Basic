li=list(map(int,input("enter list:").split( )))
l=len(li)
target_sum=7
count=0
for i in range(l-1):
   for j in range (l-1):
      
     sum=li[i]+li[j+1]
     if target_sum==sum:
        
        count=count+1
print(count)   