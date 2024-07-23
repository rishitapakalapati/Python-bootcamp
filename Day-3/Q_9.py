#9.find the elements that is present in k+n index
#k=3,n=2
#k is given by user
#input
# 3 6 8 4 61 2
#output is 2
# k=3,n=4
#80 70 54 36 72

k=int(input("enter k"))
n=int(input("enter n"))
ab=list(map(int,input().split(" ")))
le=len(ab)
if(le<k+n):
    print("error")
else:
  for i in range(0,len(ab)):
    print(ab[k+n],end=" ")
    break