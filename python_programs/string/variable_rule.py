from re import *
rule="[a-zA-Z_][A-Za-z0-9_]*"
var_name="any_one"
matcher=fullmatch(rule,var_name)
if matcher!=None:
    print("valid")
else:
    print("invalid")