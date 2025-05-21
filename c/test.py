def pal():
   
   n=int(input("enter number"))
   orginal=n
   rev=0
   if n>0:
     digit = n % 10
     rev = rev * 10 + digit
     n = n // 10
     
   
   if orginal==rev:
      print("pal")
   else:
      print("no")      
     
pal()      