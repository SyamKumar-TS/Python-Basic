def prime():
   n=int(input("enter num:"))
   if n>1:
      isprime= True
      for i in range(2,n):
         if n%i==0:
            isprime=False
      if isprime==True:
         print("prime")
      else:
         print("no")
   else:
      print("no")            
prime()      
            
      