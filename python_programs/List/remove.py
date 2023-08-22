birds=["peacock","pigeon","sparrow","duck"]
val=input("enter the name to be searched:")
for i in birds:
    if(i==val):
        birds.remove(i)
print(birds)