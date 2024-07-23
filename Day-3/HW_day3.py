#1.Find even or odd
n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")

#2.Greatest of 3
a=int(input("Enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a>b and a>c:
    print(a,"is greatest")
elif b>a and b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")

#3.find sum of all elements in an array
m=list(map(int,input().split(",")))
sum=0
for i in m:
    sum+=1
print(sum)

#4) find peek element in an array
print("enter elements")
peek=list(map(int,input().split(" ")))
n=len(peek)
count=0
for i in range(1,n-1):
    if(peek[i]>peek[i-1] and peek[i]>peek[i+1]):
        count=i
        break
print(peek[count])

#print all peek elements
print("enter elements")
peek=list(map(int,input().split(" ")))
n=len(peek)
count=0
for i in range(1,n-1):
    if(peek[i]>peek[i-1] and peek[i]>peek[i+1]):
        print(peek[i],end=" ") 


#sum of n natural numbers
n=int(input("enter any number"))
sum=n*(n+1)/2
print("sum of N natural numbers",sum)

'''
5)find max element in an array
6)find 2nd max element in an array
7)reverse an array without using built in funcions
8) find the sum of squares of given number
9)find sum of squares of even and odd digits
10)check palindrome or not by using while loop
11)WAP to print first n fibonacci series.'''
