str1=input("str1:")
str2=input("str2:")
count=0
if len(str1)!=len(str2):
    print("not anagram")
else:
    for i in range(len(str1)):
        if str1[i] in str2:
            count=count+1 
if count==len(str1):
    print("anagram")
else:
    
    print("not")                   
