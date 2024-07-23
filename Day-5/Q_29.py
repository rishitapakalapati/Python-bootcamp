#give input as hello123,print the sum of 123 from the input
vowels='aeiouAeiou'
consonants="bcdfghjklmnpqrstvwxyz"
check="0123456789"
i="hello123"
ans=0
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
print(ans)

#H.W-reverse the no's present in a given string(ex:1234-o/p:4321)
vowels='aeiouAeiou'
consonants="bcdfghjklmnpqrstvwxyz"
check="0123456789"
i="hello1234"