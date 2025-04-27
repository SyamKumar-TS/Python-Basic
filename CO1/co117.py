mydict={"red" :2,"blue":5,"green":4}
l1=list(mydict.items())
l1.sort()
dict1= dict(l1)
print("ascending",dict1)
l2=list(mydict.items())
l2.sort(reverse= True)
dict2=dict(l2)
print("des",dict2)
