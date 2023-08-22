from re import *
rule="[a-zA-Z][a-zA-Z0-9$_]{1,15}"
var_name="pu_name_"
matcher=fullmatch(rule,var_name)
if matcher!=None:
    print("valid")
else:
    print("invalid")

