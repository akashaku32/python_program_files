import re
# text="aaabbb"
# print(re.search("[a]{3}",text))
# text="abcd0888"
# print(re.search("[a-z]{3}",text))
text="abdcDCBD"
print(re.search("[a-z]{4}[A-Z]{4}",text))