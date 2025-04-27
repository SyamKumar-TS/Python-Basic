str1=input("enter str1")
str2=input("enter str2")
x=len(str1)
y=len(str2)
str3=str2[0]+str1[1: x]+" "+str1[0]+str2[1 :y]
print(str3)