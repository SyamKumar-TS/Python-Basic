str=input("enter the string:")
list=["a","e","i","o","u"]
count=0
for i in range(len(list)):
        if list[i] in str:
            count=count+1
print(count)            