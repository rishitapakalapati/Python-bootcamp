#reverse of a number(IMP!!)
n=int(input())
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(rev)
print(type(rev))
print(int(rev))