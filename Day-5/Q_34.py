'''
pattern printing
*****
*****
*****
*****
*****
'''

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print( )

for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print( )

for i in range(10):
    for j in range(10):
        if i==j:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print( )

for i in range(10):
    for j in range(10):
      print("*",end=" ")
    print( )

for i in range(10):
    for j in range(i+1):
      print("*",end=" ")
    print( )

for i in range(10):
    for j in range(10-i):
      print("*",end=" ")
    print( )  