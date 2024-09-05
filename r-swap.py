'''a=int(input('enter a number'))
b=int(input('enter a second number'))
c=0
c=a
a=b
b=c
print('swapping of two numbers done successfully')
print('now the values of a:',a,'now the value of b:',b)
#---------------------swapping---------------------------------------

a=int(input('enter the a value'))
b=int(input('enter the b value'))
a=a+b
b=a-b
a=a-b
print('a:',a,'b:',b)
---------------------------even or odd-------------------------------

n=int(input('enter a number'))
if n%2==0:
    print('n is a even number')
else :
    print('n :',n,'is a odd number')
-----------------------------positive or negative----------------

n=int(input('enter the number'))
if n>=0:
    print('the n:',n,'is a positive number')
else:
    print('the n:',n,'is a negative number')
----------------------sum of digits------------------------------'''
n=int(input('enter the number:'))
sum=0
while(n>0):
    t=n%10
    sum=sum+t
    n=n/10
print(sum)
    
