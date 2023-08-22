lst=[1,2,4,6]
l1=0
while(l1<len(lst)):
    if(lst[0]!=1):
        print("1")
        break
     
    elif(lst[l1+1]-lst[l1]==1):
        l1+=1
    else:
        print(lst[l1]+1)
        break
