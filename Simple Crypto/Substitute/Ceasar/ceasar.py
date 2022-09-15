phrase="ynkooejcpdanqxeykjrbdofgkq"

encripted=list(phrase.strip(" "))
print(encripted)
for i in range(26):
    flag=[]
    for x in encripted:
        if(ord(x)+i > ord("z")):
            flag.append(chr((ord(x)+i)-26))
        else:
            flag.append(chr((ord(x)+i)))
    print("".join(flag))
