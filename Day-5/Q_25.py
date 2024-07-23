#25. check how many vowels are in a string
a=input()
vowels='aeiouAeiou'
count=0
for i in a:
    if i in vowels:
      count+=1
print(count)
