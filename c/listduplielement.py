list1=list(input("enter elements:").split())
list2=[]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] ==list1[j]:
            list2.append(list1[i])
print(list2)
list3=[]
for item in list1:
    if item not in list2:
        list3.append(item)
for k in range(len(list2)):
    list3.append(list2[k])        
print(list3)        
        

             