#4.print even positive,even negative,odd positive,odd negative
a=int(input("enter a"))
if(a%2==0 and a>0):
    print("a is even positive")
elif(a%2==0 and a<0):
    print("even negative")
elif(a%2!=0 and a>0):
    print("odd positive")
else:
    print("odd negative") 