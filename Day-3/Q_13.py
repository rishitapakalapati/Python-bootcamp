#13.Replace the elements in an array with avg of max and min element
print("Enter array elements")
ab=list(map(int,input().split(" ")))
maxi=ab[0]
mini=ab[0]
avg=0
for i in range(len(ab)):
    if ab[i]>maxi:
        maxi=ab[i]
for i in range(len(ab)):
    if ab[i]<mini:
         ab[i]<mini
         mini=ab[i]
avg=(maxi+mini)//2
for i in range(len(ab)):
    ab[i]=avg
print(ab)