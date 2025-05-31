list1=list(input("enter list:").split())
element=input("enter the element:")
count=0
j=len(list1)
for k in range(j):
    
    for i in range (0,len(list1[k])):
        if list1[k][i]==element:
          count=count+1
'''for i in range (len(list1[1])):
    if list1[1][i]==element:
        count=count+1 '''       
print(count)    