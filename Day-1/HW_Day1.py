#basic prime no program
num=int(input("enter any number"))
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")

#prime no using square root method
from math import sqrt
n = int(input("Enter any number"))
flag = 0
if(n > 1):
	for k in range(2, int(sqrt(n)) + 1):
		if (n % k == 0):
			flag = 1
		break
	if (flag == 0):
		print(n," is a Prime Number!")
	else:
		print(n," is Not a Prime Number!")
else:
	print(n," is Not a Prime Number!")

#check whether given no is palindrome or not
s=input("enter any name")
reverse = s[::-1]
if (s == reverse):
    print("palindrome")
else:
    print("not a palindrome")

n=int(input())
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
if(temp==rev):
    print("palindrome")
else:
    print("not a palindrome")

#check whether given no is Armstrong or not
n=int(input("enter any number"))
s=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+(r**b)
    n=n//10
if s==sum1:
    print("armstrong number")
else:
    print("not")
  
#find sum of 1st n natural nos
n=int(input("enter any number"))
value=0
for i in range(1,n+1):
    value=value+i
print("sum of N natural numbers",value)