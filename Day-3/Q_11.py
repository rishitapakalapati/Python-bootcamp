# 11.Find the max element in the given list
print("Enter list elements")
ab=list(map(str,input().split(" ")))
maxi=ab[0]
for i in range(len(ab)):
    if(ab[i]>maxi):
        maxi=ab[i]
print(maxi)