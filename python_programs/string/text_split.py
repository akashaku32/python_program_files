text="RationalPrime"
l=[]
for i in range(len(text)):
    if text[i].isupper():
        l.append(i)
for i in range(len(text)):
    for j in range(i):
        if((l[0]+j)<=l[1] and i<=l[1]):
            print(text[l[0]+j].upper(),end="")
        # if(l[1]+j!=(len(text)-1)):
    for k in range(i):
        if((l[1]+k)<(len(text)) and i<=l[1]):
            print(text[l[1]+k].upper(),end="")
        
    print()

        
        
    
   

# RP
# RAPR
# RATPRI
# RATIPRIM
# RATIOPRIME
# RATIONPRIME
# RATIONAPRIME
# RATIONALPRIME


