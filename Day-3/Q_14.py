#Find the missing number in an array
my_list=list(map(int,input().split(" ")))
n=len(my_list)+1
total_sum=n*(n+1)//2
list_sum=sum(my_list)
missing_num=total_sum-list_sum
print(missing_num)