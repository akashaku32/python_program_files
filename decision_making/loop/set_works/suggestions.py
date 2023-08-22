allusers=["mohanlal","fahad","dq","vijay","nivin","asif"]
dq_frndslist=["mohanlal","fahad","asif"]
asif_friendlist=["mohanlal","fahad","vijay","nivin"]
au=set(allusers)
dq=set(dq_frndslist)

mutual=dq.intersection(set(asif_friendlist))
print(mutual) 