import re

resi=input("enter a residence number")
ekm=re.search("^0484",resi)
ijk=re.search("^0480",resi)
tcr=re.search("^0487",resi)
mpr=re.search("^0494",resi)
ksd=re.search("^04994",resi)
cct=re.search("^0495",resi)
if(ekm):
    print("ekm number")
elif(ijk):
    print(" ijk number")
elif(tcr):
    print("tcr number")
elif(mpr):
    print("mpr number")
elif(ksd):
    print("ksgd number")
elif(cct):
    print("calicut number")
