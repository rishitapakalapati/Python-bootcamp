#Print all ascii values
for i in range(32,120):
    print(chr(i),end=" ")

#sum of digits in a number using ascii values

inp=input()
sum=0
for i in inp:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)  

#write a code to print all the capital letters in a given string
inp=input()
sum=" "
for i in inp:
    if(ord(i)>=65 and ord(i)<=96):
        sum+=i
print(sum)

#write a code to print all the lowercase letters in a given string
inp=input()
sum=" "
for i in inp:
    if(ord(i)>=97 and ord(i)<=122):
        sum+=i
print(sum)