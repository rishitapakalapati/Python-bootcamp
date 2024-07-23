#7.You are given with a comma seperated natural no's 1-10.Print only even no's.
a=[1,2,3,4,5,6,7,8,9,10]
count=0
for i in range(1,11,2):
    print(a[i])
    count+=1
#how many even no's in above question
print(count) 

#you are given with a space seperated integer list.Find no.of even elements and odd elements in a given list.
my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(my_list)):
      if(my_list[i]%2==0):
           even+=1
      else:
           odd+=1
print(even)
print(odd)