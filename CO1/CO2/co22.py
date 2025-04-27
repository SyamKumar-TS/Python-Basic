def fib(n):
    n1=0
    n2=1
    while n1<=n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
n=int(input("emter the num"))
print(fib(n))        