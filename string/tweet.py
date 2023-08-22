from re import *
tweets="What a game , hats off to both teams . Well done @ @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
rule="[@][a-zA-Z0-9_]+"
k=finditer(rule,tweets)
# print(k)
for i in k:
    print(i.group())

# words=tweets.split()
# for i in words:
#     matching=fullmatch(rule,i)
#     if(matching!=None):
#         print(i)
    