text="England promises to continue its aggressive approach to test cricket"
word=text.split(" ")
vowel=["a",'e','i','o','u']
for i in word:
    if i[0].lower() in vowel:
        print(i)


#list comprehension
w=[]