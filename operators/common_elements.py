lst=[2,3,4,5]
lst1=[1,3,4,8]
low=0
low_1=0

while(low<len(lst) and low_1<len(lst1)):
    
    if(lst[low]==lst1[low_1]):
        print(lst[low])
        low+=1
    elif(lst[low]<lst1[low_1]):
        low+=1
    elif(lst[low]>lst1[low_1]):
        low_1+=1



