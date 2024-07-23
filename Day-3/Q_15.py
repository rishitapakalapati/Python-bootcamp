#Find the duplicates in an array
print("Enter the elements in array")
my_list=list(map(int,input().split(" ")))
a=[]
b=[]
for element in my_list:
    if element in a and element not in b:
        b.append(element)
    else:
        a.append(element)
print(b) 