# print all the vowels followed by consonants
i=input()
vowels='aeiouAeiou'
consonants="bcdfghjklmnpqrstvwxyz"
ans=""
inp=i.lower()
for i in inp:
    if i in vowels:
      ans+=i
for i in inp:
   if i in consonants:
      ans+=i
print(ans)