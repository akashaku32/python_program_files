import re
gmail=input("enter the mail:")
k=re.search("@gmail.com$",gmail)
if(k):
    print("gmail is valid")
else:
    print("not valid")