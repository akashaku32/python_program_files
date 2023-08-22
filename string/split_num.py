text="dhoni hit 50 in his 70 match"
word=text.split(" ")
for i in word:
    if i.isdigit():
        print(i)

#using list comprehension
ws=[i for i in text.split() if i.isdigit()]
print(ws)