users=["sachin","kohli","sehwag","rahul","dhoni","raina"]
sachin_followers=["kohli","sehwag","rahul"]
for i in users:
    f=0
    for j in sachin_followers:
        if(i==j):
            f=1
    if(f!=1):
        print(i)  

