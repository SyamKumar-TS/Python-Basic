def ing(str):
 x=len(str)
 if x>2:
    if str[-3:]=="ing":
        str= str+"ly"
    else:
        str=str+"ing"    
 print(str)        
str=input("enter string ")
ing(str)
        