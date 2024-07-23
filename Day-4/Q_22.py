#22.GCD of 2 numbers
#Euclidean algorithm
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
while b!=0:
    a,b=b,a%b
print("GCD of two numbers is",a)

#LCM of 2 numbers
import math
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
if a%b==0 or b%a==0:
    print("LCM of two numbers is",a)
else:
    print(a*b) 


