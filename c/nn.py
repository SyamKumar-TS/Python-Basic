lst=input("enter list:")
w=lst.split(",")
max=len(w[0])
for i in w:
    if len(i)>max:
       max=len(i)
print(max)                   