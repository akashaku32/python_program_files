num=153
org=num
l=len(str(num))
sum=0
while(num>0):
    digit=num%10
    sum=sum+(digit**l)
    num//=10
print(sum)
if(sum==org):
    print("armstrong")
else:
    print("not armstrong")