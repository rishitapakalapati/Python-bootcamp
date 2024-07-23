#take input from user,if user enters 1 append,user enters 2-pop 3-sort 4-print len 
my_list=list(map(str,input().split(",")))
print("values are",my_list)
print("select one option:\n 1.append\n 2.pop\n 3.sort\n 4.length\n")
choice=int(input())
if(choice==1):
    my_list.append(str(input()))
    print(my_list)
elif(choice==2):
    my_list.pop()
    print(my_list)
elif(choice==3):
    my_list.sort()
    print(my_list)
else:
    print(len(my_list))