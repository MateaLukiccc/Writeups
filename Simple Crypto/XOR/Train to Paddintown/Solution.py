from inspect import currentframe
import os
from Crypto.Util.number import long_to_bytes
from multiprocessing import Pool
import re



BLOCK_SIZE = 16
FLAG = b'|||REDACTED|||'


def pad_pt(pt):
    amount_padding = 16 if (16 - len(pt) % 16) == 0 else 16 - len(pt) % 16
    return pt + (b'\x3f' * amount_padding)


#pt = pad_pt(FLAG)
key = os.urandom(BLOCK_SIZE)

ct = b''


#with open('output.txt', 'w') as f:
#    f.write(ct.hex())
    

ct=bytes.fromhex("b4b55c3ee34fac488ebeda573ab1f974bf9b2b0ee865e45a92d2f14b7bdabb6ed4872e4dd974e803d9b2ba1c77baf725")
print(ct)
knownPLAIN=b"TFCCTF{"
end2=b"??????????"
ct2=b''
j=0
for i in range(7):
        print(i)
        ct2 += (knownPLAIN[j] ^ ct[i]).to_bytes(1, 'big')
        
for i in range(7):
    ct2+=ct[i].to_bytes(1,"big")
    
c=b''
i=0
ct2=ct[-9:]
print(ct)
print(ct2)
for x in ct[-9:]:
    c+=(ct2[i]^end2[0]).to_bytes(1,"big")
    i+=1
    
    
print(ct2[:7])
print(len(ct2[:7]))
print(c)
print(len(c))

#----------------------------------------------------------------------------------------------------------------------------------#


#key=key+random+\x7fH


key=b'\xe0\xf3\x1f}\xb7\t\xd7'+c
ct=bytes.fromhex("b4b55c3ee34fac488ebeda573ab1f974bf9b2b0ee865e45a92d2f14b7bdabb6ed4872e4dd974e803d9b2ba1c77baf725")
knownPLAIN=b"TFCCTF{"
print("Duzina kljuca je: ",len(key))

j=0
while True:
    ct2=b''
    for i in range(len(ct)):
        ct2 += (key[j] ^ ct[i]).to_bytes(1, 'big')
        j += 1
        j %= 16
    key=b'\xe0\xf3\x1f}\xb7\t\xd7'+os.urandom(9)
    try:
                #TFCCFF{...._h4s_l3......4t10n}
        #if(re.search("TFCCTF{[a-zA-Z0-9!@#$%^&*()_\-+=:;<,>.?\/]+}",ct2.decode("utf-8")) and "_h4s_l3" in ct2.decode("utf-8")):
            
            print(ct2.decode("utf-8"))
    except:
        pass
    ct2=b''



    #TFCCTF{]oEi☺}#9S_h4s_l3Os)B↔<H{I4t10n}?
    #TFCCTF{xxxxxxxS_h4s_l3OxxxxxxxxI4tion}
    #there are 10?