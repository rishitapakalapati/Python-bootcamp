#Print the unique characters in a string
i=input()
vowels='aeiouAeiou'
consonants="bcdfghjklmnpqrstvwxyz"
ans=""
inp=i.lower()
for i in inp:
    if (i not in ans):
      ans+=i
print(ans)
