#10.(cyclic rotation list)Print the element in a particular index but condition is cyclic printing
#k=3
#3 6 8 4 61 2
#op:4
#k=8
#80 70 540 360 72
#op:36

k=int(input("enter k"))
ab=list(map(int,input().split(" ")))
n=len(ab)
i=k%n
print(ab[i]) 