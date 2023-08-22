lst=[1,3,5,7,9]
low=0
upp=len(lst)
val=9
f=0
while(low<len(lst)):
    mid=(low+upp)//2
    if(val==lst[mid]):
        print("element found",mid+1)
        f=1
        break
    elif(val<lst[mid]):
        upp=mid-1
    elif(val>lst[mid]):
        low=mid+1
if(f==0):
    print("not found")