#w.a.p to print all the consonants
n=input()
vowels='aeiouAeiou'
count=0
for i in n:
   if i not in vowels:
      count+=1
print(count)
#another way:
vowels='aeiouAeiou'
consonants="bcdfghjklmnpqrstvwxyz"
count=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in vowels):
        count+=1
print(count)
for i in inp:
    if(i in consonants):
        count+=1
print(count)
