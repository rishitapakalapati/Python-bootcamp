#Print upper triangular matrix.
# print lower triangular matrix.
# Print rhombus.
# print parallelogram:
''' ***
      ***
        *** '''
#print number pyramid
 

#lower 
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print( )

#upper
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print( )


#number pyramid
n=int(input())
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end="")
        num=num+1
    print()