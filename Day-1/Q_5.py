'''
5.mr z is selected for olympics he is participating in swimming competition only one
winner is selected in the competition 
MR X mr y are friends of z.mr x is part badminton, mr y in table tennies,
according to the selection commite the requirement of badmintion
height 140 cms
weight factors of 2
body fat < than 12%
according to selection committee
required table tennies height min 118 cm to 148cm
weight factors of no of medals won by mr z
body fat 14%
according to previous history z participated in 14 games out which he is having success rate of 50%
write a program wheather to check mr x and mr y and mr z travalled in the same plane or not '''
z=True
medals_z=(50/100)* 14
print(medals_z)
print("Badminton selection")
p1=input("enter name")
height_bad=int(input("enter height in cms"))
weight_bad=int(input("enter weight"))
bodyfat_bad=int(input("enter bodyfat"))
if(height_bad==140 and weight_bad%2==0 and bodyfat_bad<12):
    print("selected")
    x=True
else:
    print("Not selected")
    x=False
print("Table tennis selection")
p2=input("enter name")
height_ten=int(input("enter height in cms"))
weight_ten=int(input("enter weight"))
bodyfat_ten=int(input("enter bodyfat"))
if(height_ten>=118 and height_ten<=148 and weight_ten%medals_z==0 and bodyfat_ten==14):
   print("selected")
   y=True
else:
    print("Not selected")
    y=False
if( x==True and y==True and z==True):
    print("all three are travelling in the same plane")
else:
    print("No")