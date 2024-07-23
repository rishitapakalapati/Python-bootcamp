#Using for loop print 1 to 100 no.
for i in range(1,101):
     print(i,end=" ")

#Using for loop append 1 to 100 in empty list.
a=[]
for i in range(1,101):
     a.append(i)
print(a)  

#Using for loop sum of all numbers in a list
print("enter list")
my_list=list(map(int,input().split(",")))
sum=0
for i in my_list:
    sum+=i
print(sum)