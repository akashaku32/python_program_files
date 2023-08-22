word="goodmorning"
l={"a","e","i","o","u"}
c=0
n=0
for i in word:
    if(set(i).intersection(l)):
        c+=1
    else:
        n+=1
print("vowels",c)
print("consonants",n)