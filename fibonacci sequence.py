n=int(input("Enter N Number : "))
n1=0
n2=1
if n<0:
    print("Enter a positive integer")
else:
    print("Fibonacci Series")
    while n1<=n:
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3
