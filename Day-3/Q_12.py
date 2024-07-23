# 12.Find the min element in the given list
print("Enter list elements")
ab=list(map(str,input().split(" ")))
mini=ab[0]
for i in range(len(ab)):
    if(ab[i]<mini):
        mini=ab[i]
print(mini)