#sum of digits
n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r #IMP!!   
    n=n//10
print(sum)
