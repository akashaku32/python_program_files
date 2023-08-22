from re import *
violations=["kl-08-av-2794",
            "kl-08-av-4970",
            "kl-01-av-14",
            "kl-01-av-1",
            "kl-01-av-12",
            "TN-01-av-1",
            "ghz-01-avO-1",
            "0kl-01-av0-10"

            ]
rule="[k][l][-][0-9]{2}[-][a-z]{2}[-][0-9]{1,4}"
for i in violations:
    matcher=fullmatch(rule,i)
    if matcher!=None:
        print(i)
