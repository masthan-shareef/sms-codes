n=int(input("enter the num:"))
b=int(input("enter the boolean num:"))
i=1
if b==1:
    while(n>=i):
        r="*"
        print(r*i)
        i=i+1
elif b==0:
    while(n>0):
        r="*"
        print(r*n)
        n=n-1
