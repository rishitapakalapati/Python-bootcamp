#23.Prime number using square root(most optimised code for prime number)
a=int(input("enter any number"))
r=a**0.5
count=0
if a==1:
     print("not a prime number")
elif a==2:
     print("prime number")
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break
if count==0:
        print("prime")
else:
    print("not prime") 