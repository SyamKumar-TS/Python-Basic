str=input("enter the string:")
n=len(str)
if n>2:
   if str[-3:]=="ing":
      print(str+"ly")
   else:
      print(  str+"ing")   